import pandas as pd

def load_data(true_path, observed_path):
    """Load data from true and observed Excel files"""
    try:
        true_df = pd.read_excel(true_path, skiprows=0, skipfooter=2).drop([0])  # Skip the first row containing "Graded by:"
        observed_df = pd.read_excel(observed_path, skiprows=0, skipfooter=2).drop([0])  # Skip the first row containing "Graded by:"

        # Drop columns with NA values
        true_df = true_df.dropna(axis=1, how='any').set_index("Chat #")
        observed_df = observed_df.dropna(axis=1, how='any').set_index("Chat #")
        
        return true_df, observed_df
    
    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None

def calculate_similarity(true_df, observed_df):
    """Calculate similarity between true and observed values"""
    
    # Calculate overall similarity based on non-empty cells
    identical_cells = (true_df == observed_df).sum().sum()
    total_cells = true_df.size
    overall_similarity = (identical_cells / total_cells) * 100
    
    return overall_similarity

def calculate_similarity_per_row(true_df, observed_df):
    """Calculate similarity between corresponding rows in true and observed dataframes"""
    similarities_per_row = []
    for row_title, (true_row, observed_row) in zip(true_df.index, zip(true_df.itertuples(index=False), observed_df.itertuples(index=False))):
        row_identical_cells = sum(x == y for x, y in zip(true_row, observed_row))
        row_total_cells = len(true_row)
        row_similarity = (row_identical_cells / row_total_cells) * 100
        similarities_per_row.append((row_title, row_similarity))  # Store row index and similarity
    return similarities_per_row

if __name__ == "__main__":
    true_excel_path = "Manual Real Chat Grading [Confidential].xlsx"  # Path to the true values Excel file
    observed_excel_path = "Manual Real Chat Grading [Confidential].xlsx"  # Path to the observed values Excel file
    
    # Load data
    true_df, observed_df = load_data(true_excel_path, observed_excel_path)

    if true_df is not None and observed_df is not None:
        # Ensure both dataframes have the same shape
        if true_df.shape != observed_df.shape:
            print("Error: Shapes of true and observed dataframes do not match.")
        else:
            # Calculate overall similarity
            overall_similarity = calculate_similarity(true_df, observed_df)
            print(f"Overall Similarity between spreadsheets: {overall_similarity:.2f}%")
            
            # Calculate similarity per row
            similarities_per_row = calculate_similarity_per_row(true_df, observed_df)
            print("Similarity per row:")
            for row_title, similarity in similarities_per_row:
                print(f"{row_title}: {similarity:.2f}%")
    else:
        print("Error: Dataframes could not be loaded.")

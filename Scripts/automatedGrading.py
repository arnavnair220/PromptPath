import pandas as pd
import automatedAssitantFeeder
import matplotlib.pyplot as plt
import seaborn as sns

"""
Instructions:
Run this script, then add the range of chats you want to run the script on.

Ex: python automatedGrading.py
Start: 1
End: 3
"""


def load_data(true_path, chatIDStart=0, chatIDEnd=1):
    """Load data from true Excel file"""
    try:
        true_df = pd.read_excel(true_path, skipfooter=2).drop([0,1])  # Skip the first row containing "Graded by:"
        # Drop columns with NA values (ungraded chats // unfinished grading)
        true_df = true_df.set_index("Rubric Questions").dropna(axis=1, how='any')
        # User Selected Chats
        true_df = true_df.iloc[:, chatIDStart:chatIDEnd]
        
        observed_df = automatedAssitantFeeder.feedChats("UW Chat Transcripts.xlsx", chatIDStart, chatIDEnd)
        observed_df.insert(0, "Rubric Questions", true_df.index.to_list())
        observed_df = observed_df.set_index("Rubric Questions")
        print(observed_df)

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


def visualize_similarity(similarities_per_row, overall_similarity, threshold=0):
    """Visualize similarity per row using a heatmap"""
    # Filter out rows with similarity below the threshold
    similarities_per_row = [(row_title, similarity) for row_title, similarity in similarities_per_row if similarity >= threshold]

    # Extract rubric questions and similarities
    rubric_questions = [row[0] for row in similarities_per_row]
    similarities = [row[1] for row in similarities_per_row]

    # Create a DataFrame for visualization
    df_visualization = pd.DataFrame({'Rubric Questions': rubric_questions, 'Similarity': similarities})

    # Calculate vmin and vmax for color scale
    vmin = 0
    vmax = max(similarities)

    # Create a figure
    plt.figure(figsize=(16, 10))  # Increase figure size

    # Create the heatmap
    ax = plt.subplot(111)  # Create subplot for heatmap
    sns.heatmap(df_visualization.set_index('Rubric Questions'), cmap='RdYlGn', annot=True, fmt=".2f", vmin=vmin, vmax=vmax)
    plt.title('Similarity per Rubric Question')
    plt.xlabel('Chat IDs')
    plt.ylabel('Rubric Questions')
    plt.xticks(rotation=45, fontsize=8)  # Rotate labels and adjust font size
    plt.yticks(rotation=0, fontsize=8)   # Adjust font size

    # Add a text annotation for overall similarity in the bottom left corner
    ax.annotate(f"Overall Similarity: {overall_similarity:.2f}%", xy=(0, 0), xycoords='axes fraction', fontsize=10,
                xytext=(20, 20), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="lightblue", ec="blue", lw=1))

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    chatIDStart = int(input("Start: "))-1
    chatIDEnd = int(input("End: "))
    true_excel_path = "Manual Real Chat Grading [Confidential].xlsx"  # Path to the true values Excel file
    
    # Load data
    true_df, observed_df = load_data(true_excel_path, chatIDStart, chatIDEnd)

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

            #Visualization
            visualize_similarity(similarities_per_row, overall_similarity)
    else:
        print("Error: Dataframes could not be loaded.")

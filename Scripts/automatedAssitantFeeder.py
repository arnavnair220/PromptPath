import openai
import pandas as pd
import time
import numpy as np

#OpenAI API key
client = openai.OpenAI(api_key = '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')
assistant_id = 'asst_jET1LLOxddvcVqnp2LiHG8NX'

def ask_assistant(prompt):
    try:
        assistant = client.beta.assistants.retrieve(assistant_id)
        thread = client.beta.threads.create()
        message = client.beta.threads.messages.create(thread_id=thread.id, role = "user", content = prompt)
        run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant.id)
    
        while run.status == "queued" or run.status == "in_progress":
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id,
                run_id=run.id,
            )
        time.sleep(0.5)

        messages = client.beta.threads.messages.list(thread_id=thread.id)
    
        return messages.data[0].content[0].text.value
    
    except Exception as e:
        print(f"Error getting messages from OpenAi: {e}")
        return None

def feedChats(file, chatIDStart, chatIDEnd):
    chats = pd.read_excel(file)
    chats = chats.loc[chatIDStart-1:chatIDEnd-1]
    one_hots = []
    for x in chats.iterrows():
        response = ask_assistant((x[1][0]))
        one_hot = eval(response.splitlines()[-1])
        one_hots.append(one_hot)
    return oneHotsToDF(one_hots)

def oneHotsToDF(one_hots):
    npArray = (np.array(one_hots, dtype=object)).T
    #npArray = np.pad(npArray, ((0, ??),(0, 0)), 'constant', constant_values=(0))
    df = pd.DataFrame(npArray)
    df.columns += 1
    return df

if __name__ == "__main__":
    None
    #df = feedChats("UW Chat Transcripts.xlsx")
    #print(df)

    #chats = pd.read_excel("UW Chat Transcripts.xlsx")
    #response = ask_assistant(chats["Chat Transcript"][0])
    #print(response)


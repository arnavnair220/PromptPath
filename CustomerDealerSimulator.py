import openai
import time
import sys


client = openai.OpenAI(api_key = '')
dealer_id = 'asst_kMljCzTiDhpfZNKWivuFALFk'
customer_id = 'asst_PkV6KxUQ0DJuEHa1HmOJ5PLD'

def ask_assistant(prompt, isDealer, thread=None):

    if isDealer:
        assistant_id = dealer_id
    else:
        assistant_id = customer_id

    try:
        assistant = client.beta.assistants.retrieve(assistant_id)
        if thread == None:
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
        return messages.data[0].content[0].text.value, thread


    except Exception as e:
        print(f"Error getting messages from OpenAi: {e}")
        return None


def converse(convoLength):
    dealerOutput, dealerThread = ask_assistant("hi", True)
    print("DEALER: " + dealerOutput + "\n")
    customerOutput, customerThread = ask_assistant(dealerOutput, False)
    print("CUSTOMER: " + customerOutput + "\n")
    
    for i in range(convoLength-1):
        dealerOutput, dealerThread = ask_assistant(customerOutput, True, dealerThread)
        print("DEALER: " + dealerOutput + "\n")
        customerOutput, customerThread = ask_assistant(dealerOutput, False, customerThread)
        print("CUSTOMER: " + customerOutput + "\n")



if __name__ == "__main__":
    args = sys.argv
    
    convoLength = int(input("Conversation Length: "))

    if len(args) == 1:
        converse(convoLength)
    else:
         with open(str(args[1]) + '.txt', 'w') as f:
            sys.stdout = f
            converse(convoLength)
            sys.stdout = sys.__stdout__

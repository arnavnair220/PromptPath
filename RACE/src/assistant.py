from openai import OpenAI
from dotenv import load_dotenv

import sys

## importing helpers functions
from helpers import *

def main():
  
  if (len(sys.argv) != 3):
    sys.exit("Usage: python assistant.py <prompt_path> <data_path>")

  with open(sys.argv[1]) as p:
    prompt = p.read()

  with open(sys.argv[2]) as d:
    data = d.read()

  # print(f"Prompting with:\n{prompt}")

  load_dotenv()

  # default grab openAI key from env
  # default grabs env "OPENAI_API_KEY"
  client = OpenAI()

  # init assistant
  assistant = client.beta.assistants.create(
    name="promptPath assistant",
    instructions=prompt,
    model="gpt-4-turbo-preview"
  )

  # init thread
  thread = client.beta.threads.create()

  # prompting part
  run = submit_message(assistant.id, thread, data, client)

  wait_on_run(run, thread, client)
  pretty_print(get_response(thread, client))
  client.beta.assistants.delete(assistant.id)

if __name__ == "__main__":
  main()
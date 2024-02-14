from openai import OpenAI
from dotenv import load_dotenv

import os
import json
import sys

## importing helpers functions
from helpers import *

def main():
  
  if (len(sys.argv) != 3):
    print("Usage: python assistant.py <prompt_path> <data_path>")

  f = open(sys.argv[1])
  prompt = f.read()
  f.close()

  f = open(sys.argv[2])
  data = f.read()
  f.close()

  print(f"Prompting with:\n{prompt}")

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

  # prompting part!
  f = open("./data/convo1.txt")
  data = f.read()
  f.close()

  run = submit_message(assistant.id, thread, data, client)

  wait_on_run(run, thread, client)
  pretty_print(get_response(thread, client))


if __name__ == "__main__":
    main()
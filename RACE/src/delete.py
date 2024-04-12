from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

my_assistants = client.beta.assistants.list(
    order="desc",
    limit="100", # type: ignore
)

my_assistants = map(lambda x : x.id,filter(lambda x : x.name == "Math Tutor", my_assistants))
# print(list(my_assistants))

for id in my_assistants:
  print(id)
  client.beta.assistants.delete(id)


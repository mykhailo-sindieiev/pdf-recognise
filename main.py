from google import genai
from google.genai import types

import os
from dotenv import load_dotenv

load_dotenv() 

API_KEY=os.getenv("GEMINI_API_KEY")

client = genai.Client()

# for m in client.models.list():
#     for action in m.supported_actions:
#         if action == "generateContent":
#             print(m.name)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="explain me in 10 words what is ai",
)
print(response)

client.close()
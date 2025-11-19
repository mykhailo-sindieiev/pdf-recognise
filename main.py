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

# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents="explain me in 10 words what is ai",
# )
# print(response)

YOUR_PDF_PATH = 'pentest.pdf'
YOUR_PDF_MIME_TYPE = 'application/pdf'
with open(YOUR_PDF_PATH, 'rb') as f:
    image_bytes = f.read()

for chunk in client.models.generate_content_stream(
    model='gemini-2.5-flash',
    contents=[
        'Make a summary of the attached pdf report. Extract vulnerabilities and list thier titles in the answer only. No more than amount of vulnerabilities in the report.',
        types.Part.from_bytes(data=image_bytes, mime_type=YOUR_PDF_MIME_TYPE),
    ],
):
    print(chunk.text, end='')

client.close()
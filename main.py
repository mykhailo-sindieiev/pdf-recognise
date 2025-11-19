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

response = client.models.generate_content(
    model='gemini-2.5-flash',
    config=types.GenerateContentConfig(
        response_mime_type='application/json',
        response_schema={
            'required': [
                'name',
                'description',
                'severity',
            ],
            'properties': {
                'name': {'type': 'STRING'},
                'description': {'type': 'STRING'},
                'severity': {'type': 'STRING'},
            },
            'type': 'OBJECT',
        },
    ),
    contents=[
        'Extract vulnerabilities from the provided penetration report and list the data about them in the required answer format. If there many vulnerabilities, make a list of the objects. Extract all vulnerabilities from the report',
        types.Part.from_bytes(data=image_bytes, mime_type=YOUR_PDF_MIME_TYPE),
    ],
)
print(response.text)

client.close()
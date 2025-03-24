from flask import Flask, request, jsonify
import base64
from openai import OpenAI
from io import BytesIO
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)

client = OpenAI()
CORS(app) 

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages = [
        {
            'role': 'user',
            'content' : [
                {
                    'type' : 'text', 
                    'text': 'What is in this image?'
                },
                {
                    'type' : 'image_url',
                    'image_url': {
                        'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKfTzRiDc-HYxu6l5_jZpSqkOsctxH-oMesA&s',
                        'detail': 'low',
                    },
                },
            ],
    
        }
    ],
    max_tokens=300,
)

print('Completion Tokens:', response.usage.completion_tokens)
print('Prompt Tokens:', response.usage.prompt_tokens)
print('Total Tokens', response.usage.total_tokens)
print(response.choices[0].message)
print(response.choices[0].message.content)

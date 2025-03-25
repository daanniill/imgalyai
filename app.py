from flask import Flask, request, jsonify
import base64
from openai import OpenAI
from io import BytesIO
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)

client = OpenAI()
CORS(app) # Allows requests from the Chrome Extension

global processed_text = "" # defines a variable for processed text to be stored


@app.route("/process_image", methods=["POST"])
def process_image():
    data = request.json
    img_data = data.get("image")

    if not img_data:
        return jsonify({"error": "No image data receieved"}), 400

    try:
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages = [
                {
                    'role': 'user',
                    'content' : [
                        {
                            'type' : 'text', 
                            'text': 'Analyze the image. If the image is of a question, answer it.'
                        },
                        {
                            'type' : 'image_url',
                            'image_url': {
                                'url': f'data:image/png;base64, {img_data}',
                                'detail': 'low',
                            },
                        },
                    ],
            
                }
            ],
            max_tokens=300,
        )
        processed_text = response["choices"][0]["message"]["content"]

        return jsonify({"message": "Image processed succesfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get_text", methods=["GET"])
def get_text():
    return processed_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

    
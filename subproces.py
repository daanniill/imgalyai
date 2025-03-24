import base64
import time
from io import BytesIO
from openai import OpenAI
from PIL import Image, ImageGrab

client = OpenAI()

# encodes images as string data to be sent to gpt
def encode_image(image):
    buffered = BytesIO() # creates a memory buffer to handle the image in memory
    image.save(buffered, format="PNG") # saves the image to memory buffer
    return base64.b64encode(buffered.getvalue()).decode('utf-8') # returns an encoded image from buffer

def get_clipboard_img():
    try:
        image = ImageGrab.grabclipboard() # tries to grab an image from the clipboard
        if image:
            return encode_image(image)
    except Exception as e:
        print("Error: Couldn't access clipboard", e)
    return None

def send_img_to_server(img_base64):
    url = "http://localhost:5000/process_image"
    data = {"image": img_base64}
    try:
        response = requests.post(url, json=data)
        print("Server response:", response.json())
    except Exception as e:
        print("Error sending image:", e)



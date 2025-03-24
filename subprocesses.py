import base64
import requests
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
    url = "http://localhost:5000/process_image" # defines the server url
    data = {"image": img_base64} # packages the data and labels it
    try:
        response = requests.post(url, json=data) # sends out post request with the data
        print("Server response:", response.json()) # prints status statement
    except Exception as e:
        # Exception handling
        print("Error sending image:", e)

# constant image monitoring, checks clipboard for new images
# ensures that the script only runs if exectuted directly
if __name__ == "__main__":
    print("Monitoring clipboard for images...")
    last_img = None # variable that keeps track of last image grabbed from clipboard
    while True:
        img_base64 = get_clipboard_img()
        # if there is a new image and it exists, replace last_img with it and send it to the server. Else do nothing
        if img_base64 and img_base64 != last_img:
            print("New image detected, sending to server...")
            send_img_to_server(img_base64)
            last_img = img_base64
        time.sleep(5) # Checks every 5 seconds




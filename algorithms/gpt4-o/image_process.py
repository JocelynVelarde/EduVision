import base64
from tkinter import Image
from openai import OpenAI 
import streamlit as st

## Sample text request
MODEL="gpt-4o"
IMAGE_PATH = "assets/images/lesson plan.jpg"
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

## Base 64 image processing
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image(IMAGE_PATH)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "Help me to create a lesson plan for the next class!"},
        {"role": "user", "content": [
            {"type": "text", "text": "Specify the activities for the next class."},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{base64_image}"}
            }
        ]}
    ],
    temperature=0.0,
)

print(response.choices[0].message.content)
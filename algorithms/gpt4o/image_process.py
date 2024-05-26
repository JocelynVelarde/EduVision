import base64
import streamlit as st
from openai import OpenAI

# OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Function to encode image
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode("utf-8")

# Function to create lesson plan
def create_lesson_plan(image_file, model="gpt-4o"):
    base64_image = encode_image(image_file)

    response = client.chat.completions.create(
        model=model,
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

    return response.choices[0].message.content
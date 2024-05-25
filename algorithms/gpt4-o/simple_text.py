import base64
import os
from tkinter import Image
from openai import OpenAI 
import streamlit as st

## Sample text request
MODEL="gpt-4o"
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

completion = client.chat.completions.create(
  model=MODEL,
  messages=[
    {"role": "system", "content": "Help me to create a lesson plan for the next class!"}, 
    {"role": "user", "content": "Hello! Could you solve 2+2?"}  
  ]
)

print("Assistant: " + completion.choices[0].message.content)
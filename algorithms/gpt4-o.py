from openai import OpenAI 
import streamlit as st

## Sample text request
MODEL="gpt-4o"
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

completion = client.chat.completions.create(
  model=MODEL,
  messages=[
    {"role": "system", "content": "You are a helpful assistant. Help me with my math homework!"}, 
    {"role": "user", "content": "Hello! Could you solve 2+2?"}  
  ]
)

print("Assistant: " + completion.choices[0].message.content)
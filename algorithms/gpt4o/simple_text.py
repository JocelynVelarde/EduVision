from tkinter import Image
from openai import OpenAI 
import streamlit as st

def ask_chat(select_course, select_course_level, select_duration_course, select_hours_per_day):
  ## Sample text request
  MODEL="gpt-4o"
  client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

  completion = client.chat.completions.create(
    model=MODEL,
    messages=[
      {"role": "system", "content": "Your role is to generate a detailed plan study for the professor, including proposed activities, topics, quizzes, exams, and homework"}, 
      {"role": "user", "content": "Help me to create a lesson plan for " + select_course + " class" + " at " + select_course_level + " level" + " for " + select_duration_course + " with " + select_hours_per_day + " per day"}  
    ]
  )

  return completion.choices[0].message.content

  #print("Assistant: " + completion.choices[0].message.content)
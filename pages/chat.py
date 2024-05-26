import streamlit as st
from openai import OpenAI
from algorithms.gpt4o.simple_text import ask_chat
from algorithms.gpt4o.image_process import create_lesson_plan

st.set_page_config(
        page_title="EduVision",
        page_icon="📒",
)

submit = False
submit_photo = False

st.title('Create a Study Plan with EduVision')

st.divider()

st.subheader(':green[Fill out the fields to start generating]')

with st.form("Study Plan Form"):
   select_course = st.selectbox(
       "Select course", ["Math", "Science", "English"])
   select_course_level = st.selectbox(
       "Select course level", ["Elementary", "High School", "College"])
   select_duration_course = st.selectbox("Select duration of course", [
                                         "1 month", "2 months", "3 months"])
   select_hours_per_day = st.selectbox(
       "Select time per class", ["40 minutes", "1 hour", "2 hours", "3 hours"])
    

   
   submitted = st.form_submit_button("Generate")

   if submitted:
      submit = True
      st.warning("Generating study plan...")
      st.write(ask_chat(select_course, select_course_level, select_duration_course, select_hours_per_day))


st.divider()

st.subheader(':green[Upload a picture with class content to start generating]')

with st.form("Study Plan Image Form"):
   input_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    

   
   submitted = st.form_submit_button("Generate")

   if submitted:
      submit_photo = True
      st.warning("Generating study plan...")
      result = create_lesson_plan(input_image)
      st.write(result)
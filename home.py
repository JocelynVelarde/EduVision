import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
        page_title="EduVision",
        page_icon="📒",
)

st.title(':green[Welcome to EduVision 📒]')

st.write('Teaching has never been easier! EduVision is a AI computer vision platform that allows the usage of several dynamic tools to power up your lesson content')

st.subheader('We have two main infrastructure features:')

col1, col2 = st.columns(2)
col1.subheader(":green[Classroom Attention]")
col1.divider()
col1.write("- Use of computer vision tools to monitor sentiment analysis and attention levels of students")
col1.write("- Fetch data on a dynamic dashboard to view different metrics")
col1.write("- Mantain privacy of students using only tags and not saving biometric data")
col1.write("- Generate reports and reccomendations in relation to the results from lessons")
col1.write("- Identify in which section of the class the students where most engaged, and what was the content being displayed")

col2.subheader(":green[Generate Content]")
col2.divider()
col2.write("- Use of generative artificial intelligence to create content for your lessons")
col2.write("- Direct voice interaction and conversation with an assistant to generate the desired content")
col2.write("- Text integration and audios to increase dynamic interaction")
col2.write("- Selection between creating a study plan or lesson content by filling a form")
col2.write("- Visualization of study plan on a calendar depending on the time and content of the lesson")

st.divider()
st.subheader(":green[We combine the use of several tools to make your teaching experience easier]")

col3, col4 = st.columns(2)
col3.subheader("📌 Computer Vision")
col3.write("1. OpenCV")
col3.write("2. Example")


col4.subheader("📌 Natural Language Processing")
col4.write("1. gpt-3.5 turbo")
col4.write("2. Example")

col5, col6 = st.columns(2)
col5.subheader("📌 Generative AI")
col5.write("1. gpt4-o")
col5.write("2. Example")

col6.subheader("📌 Data Visualization")
col6.write("1. Plotly")
col6.write("2. Example")

st.divider()
st.subheader(":green[Get Started]")
st.page_link("pages/instructions.py", label="See Instructions 🚀")

st.divider()

st.markdown("<span style='margin-left: 250px; font-weight: 20px; font-size: 15px'>Thanks for using EduVision 📒</span>", unsafe_allow_html=True)


import base64
import streamlit as st
from DataManager import DataManager
from algorithms.gpt4o.pptx_genai import generate_slide_titles, generate_slide_content, create_presentation

mongo = DataManager()

st.set_page_config(
        page_title="EduVision",
        page_icon="📒",
)

st.title('Instructions')

st.write('Welcome to EduVision, here is where your journey starts!')

st.write('Wanna know how to use it?')

col1, col2  = st.columns(2)

col1.subheader(":green[Create or Improve Study Plans]")
col1.divider()
col1.write("1) Go to the slide panel and look out for the section named Chat")
col1.write("- If you want to generate content fil out the forms with the information neeeded, once all filled out click generate!")
col1.write("- To improve your study plan scroll down and you will see a the section called :green[*Upload a picture with class content to start generating*] Drop your file to the box  and click generate!")
col1.write("- If you want to generate a base plan from just a title, scroll down to the section calles :green[*Type a content topic to start generating a PPT*] Write the topic of your presentation and click generate!")
col1.write("2) Either path you choose a fresh and strategic Education plan is presented to you!")

col2.subheader(":green[Measure your classroom attention]")
col2.divider()
col2.write("1) Conect your EduVision Kit to your Computer, make sure you are connected to WiFi!")
col2.write("2) Point the camara so all of your students are in Frame, Remember to Smile!")
col2.write("3) Run the Eduvision Program and continue your normal class, don't worry EduVision is already by your side assiting you!")
col2.write("4) Once class is dismissed, stop the Eduvision Program come back to the website and look for the section panel")
col2.write("5) In here you will now see all of your Classroom Attention Data!")
col2.write("- Strategize your next class if needed or keep up the good work!")

st.divider()
st.subheader(":green[EduVision The Educational Ecosystem of the Future!]")

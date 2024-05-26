import base64
import streamlit as st
from algorithms.gpt4o.pptx_genai import generate_slide_titles, generate_slide_content, create_presentation

st.set_page_config(
        page_title="EduVision",
        page_icon="📒",
)

st.title('Instructions')
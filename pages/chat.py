import streamlit as st
from openai import OpenAI

st.set_page_config(
        page_title="EduVision",
        page_icon="📒",
)

submit = False

st.title('Create a Study Plan with EduVision')

st.divider()

st.subheader(':green[Fill out the following fields to start generating]')

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

if submit:
   client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

   if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

    if "messages" not in st.session_state:
     st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
                stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                ],
                stream=True,
                )
                response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
      

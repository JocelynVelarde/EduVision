import streamlit as st

url = 'https://www.streamlit.io/'

st.title('Home')

st.write('This is going to be our static website.')

st.page_link(url, label='Dynamic Website', icon="🚨")
import streamlit as st
import webbrowser

url = 'https://www.streamlit.io/'

st.title('Home')

st.write('This is going to be our static website.')

if st.button('Go to Panel'):
    st.write('Redirecting to Panel...')
    webbrowser.open_new_tab(url)
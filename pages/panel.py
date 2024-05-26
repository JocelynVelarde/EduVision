import base64
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from DataManager import DataManager
from algorithms.gpt4o.pptx_genai import generate_slide_titles, generate_slide_content, create_presentation

mongo = DataManager()

st.set_page_config(
        page_title="EduVision",
        page_icon="📒",
)

st.title('View Classroom Metrics')

st.divider()

data = mongo.get_data()

# Convert the data to a pandas DataFrame
df = pd.DataFrame(list(data))

# Convert the unix timestamp to a readable date format
df['date'] = pd.to_datetime(df['timestamp'], unit='s')

# Convert the timezone to CST
df['date'] = df['date'].dt.tz_localize('UTC').dt.tz_convert('US/Central')

# Extract only the time
df['time'] = df['date'].dt.time

# Now you can drop the 'date' column if you don't need it
df = df.drop(columns=['date'])

# Set the date as the index of the DataFrame
df.set_index('time', inplace=True)

# List of emotions
emotions = ["focused", "distracted", "happy", "sad", "angry", "surprise", "fear", "neutral", "disgust"]

# Plot a bar graph for each emotion
for emotion in emotions:
    st.subheader(f'{emotion.capitalize()} Over Time')
    df[emotion].plot(kind='bar')
    st.pyplot(plt)
    plt.clf()
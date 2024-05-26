import base64
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from DataManager import DataManager
from datetime import datetime
from algorithms.gpt4o.pptx_genai import generate_slide_titles, generate_slide_content, create_presentation

mongo = DataManager()

def unix_converter(unix_timestamp):
    dt_object = datetime.fromtimestamp(unix_timestamp)
    return dt_object

st.set_page_config(
        page_title="EduVision",
        page_icon="📒",
)

st.title('View Classroom Metrics')

st.divider()

st.subheader(':green[Emotions Over Time (Unix Timestamp)]')
st.write("Use our unix converter to find a specific time range.")


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
    st.bar_chart(df[emotion])

st.subheader(":green[Unix Timestamp Data Converter]")
unix_timestamp = st.number_input("Enter a Unix Timestamp", value=0)

if st.button("Convert to Date and Time"):
    st.write(unix_converter(unix_timestamp))

st.divider()
st.subheader(":green[Raw Data of Emotions and Attention Timespan]")

st.dataframe(df)

st.divider()
st.subheader(":green[Visualization of concentration span]")

import matplotlib.pyplot as plt

# Calculate the number of people distracted vs not distracted
attention_data = df[['distracted', 'focused']].sum()

# Create a pie chart
fig, ax = plt.subplots()
ax.pie(attention_data, labels=attention_data.index, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig)
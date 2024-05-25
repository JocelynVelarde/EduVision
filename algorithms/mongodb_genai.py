
from pymongo.mongo_client import MongoClient
import streamlit as st
import urllib

password = st.secrets["MONGODB_ATLAS_CLUSTER_URI"]
uri = "mongodb+srv://pollogunpao:" + urllib.parse.quote(password) + "@cluster0.ny8favk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

from pymongo.mongo_client import MongoClient
import streamlit as st
import urllib
import pymongo

password = st.secrets["MONGODB_ATLAS_CLUSTER_URI"]
uri = "mongodb+srv://pollogunpao:" + urllib.parse.quote(password) + "@cluster0.ny8favk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(uri)

db = client.lince_hack
collection = db.educaation


mydict = { "name": "John", "address": "Highway 37" }


# Send a ping to confirm a successful connection
try:
    x = collection.insert_one(mydict)
    
except Exception as e:
    print(e)





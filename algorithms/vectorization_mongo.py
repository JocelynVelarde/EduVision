import openai
import pymongo
import streamlit as st

MONGODB_ATLAS_CLUSTER_URI = st.secrets["MONGODB_ATLAS_CLUSTER_URI"]
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

client = pymongo.MongoClient(MONGODB_ATLAS_CLUSTER_URI)
db = client.sample_mflix
collection = db.movies

openai.api_key = OPENAI_API_KEY
     

ATLAS_VECTOR_SEARCH_INDEX_NAME = "default"
EMBEDDING_FIELD_NAME = "embedding_openai_nov19_23"
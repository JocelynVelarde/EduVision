
from pymongo.mongo_client import MongoClient
import streamlit as st
import urllib
import pymongo


class DataManager:
    def __init__(self):
        self.password = st.secrets["MONGODB_ATLAS_CLUSTER_URI"]
        self.uri = "mongodb+srv://pollogunpao:" + urllib.parse.quote \
            (self.password) + "@cluster0.ny8favk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = pymongo.MongoClient(self.uri)

        self.db = self.client.lince_hack
        self.collection = self.db.educaation

    def post_data(self, dic):
        # Send a ping to confirm a successful connection
        try:
            x = self.collection.insert_one(dic)

        except Exception as e:
            print(e)
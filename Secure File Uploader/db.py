from flask import Flask
from flask_pymongo import pymongo
from app import app

CONNECTION_STRING = "mongodb+srv://dbUser:1PASSword1@flask-mongodb-atlas.e8vt3.mongodb.net/file-collection-ingester?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongoDB_atlas')
user_collection = pymongo.collection.Collection(db, 'file_collection_ingester')

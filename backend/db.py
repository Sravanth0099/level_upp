# MongoDB connection logic
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')  # Update if needed
db = client['level_upp']  # Database name
users_collection = db['users']  # Collection name

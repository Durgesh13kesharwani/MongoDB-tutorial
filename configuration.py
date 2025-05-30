
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#uri = "mongodb+srv://durgesh13keshari:OKnl5Y6PWK2HV0ow@cluster0.idnxmhy.mongodb.net/todo_db?retryWrites=true&w=majority&appName=Cluster0"
uri = "mongodb+srv://testuser:testpass123@cluster0.idnxmhy.mongodb.net/todo_db?retryWrites=true&w=majority"


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db= client.todo_db
collection = db["todo_data"]

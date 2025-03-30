from pymongo import MongoClient

client = MongoClient("mongodb+srv://neerajkumar1092005:FFLrJknlUTZA8QuU@cluster0.hlt83dv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["whatsapp_chat_db"]


print("Connected to MongoDB successfully!")

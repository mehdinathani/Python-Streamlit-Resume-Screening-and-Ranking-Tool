# utils/logger.py
import os
import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables from .env.local
load_dotenv(dotenv_path=".env.local")

# Retrieve the MongoDB URI from the environment
MONGODB_URI = os.getenv("MONGODB_URI")
if not MONGODB_URI:
    raise Exception("MONGODB_URI is not set in the environment!")

# Create a new client and connect to the server using the official snippet
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

# Optionally, send a ping to confirm the connection (you can remove this in production)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error connecting to MongoDB:", e)

# Use (or create) a database named "resume_ranker" and a collection named "logs"
db = client["resume_ranker"]
logs_collection = db["logs"]

def log_action(file_name, action, ai_feedback, details=""):
    """
    Logs a user action to MongoDB with a timestamp.
    
    Parameters:
    - file_name (str): Name of the file (or empty string if not applicable)
    - action (str): Brief description of the action (e.g., "File Uploaded", "Processed Resume")
    - details (str): Additional details (optional)
    """
    timestamp = datetime.datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "file_name": file_name,
        "action": action,
        "details": details,
        "AI FeedBack": ai_feedback
    }
    logs_collection.insert_one(log_entry)

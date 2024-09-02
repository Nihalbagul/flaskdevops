from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

# Construct MongoDB URI from environment variables
mongo_user = os.environ.get("MONGO_ROOT_USERNAME")
mongo_password = os.environ.get("MONGO_ROOT_PASSWORD")
mongo_uri = f"mongodb://{mongo_user}:{mongo_password}@mongo:27017/"
client = MongoClient(mongo_uri)
db = client.flask_db
collection = db.data

@app.route('/')
def index():
    return f"Welcome to the Flask app! The current time is: {datetime.now()}"

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        data = request.get_json()
        collection.insert_one(data)
        return jsonify({"status": "Data inserted"}), 201
    elif request.method == 'GET':
        data = list(collection.find({}, {"_id": 0}))
        return jsonify(data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

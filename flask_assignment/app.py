from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import pymongo
import os 

load_dotenv()
  
MONGO_URI = os.getenv("MONGO_URI")
# Connect to MongoDB        
client = pymongo.MongoClient(MONGO_URI)

db = client.test

collection = db['flask-assignment']

app = Flask(__name__)
@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    # Insert the data into MongoDB
    collection.insert_one(form_data)
    return jsonify({"message": "Data submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
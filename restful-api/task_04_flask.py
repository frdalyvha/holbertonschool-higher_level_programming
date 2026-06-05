#!/usr/bin/python3
"""
Flask API with in-memory user storage.

Endpoints:
- / : Welcome message
- /data : list of all usernames
- /status : returns "OK"
- /users/<username> : returns user object or 404
- /add_user (POST) : adds a new user (JSON required)
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage: key = username, value = user dict
users = {}

@app.route('/')
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Return API status."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Return user data for given username or 404."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user from JSON data."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    data = request.get_json()
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    # Store the entire user object (including username)
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

#!/usr/bin/python3
"""
Flask application that renders dynamic content from JSON.
Includes routes: /, /about, /contact, /items
"""
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')

@app.route('/items')
def items():
    """Render a list of items from items.json."""
    # Get the directory of this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, 'items.json')
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

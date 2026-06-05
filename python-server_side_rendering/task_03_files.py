#!/usr/bin/python3
"""
Flask application that reads product data from JSON or CSV and displays it.
Query parameters: source (json|csv), id (optional)
"""
from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_file(filepath):
    """Read and return product list from JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def read_csv_file(filepath):
    """Read and return product list from CSV file."""
    products = []
    try:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert price to float for consistency
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except (FileNotFoundError, KeyError):
        return None

@app.route('/products')
def products():
    """Display products from JSON or CSV, optionally filtered by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validate source
    if source not in ('json', 'csv'):
        return render_template('product_display.html',
                               error="Wrong source")

    # Determine file path based on source
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if source == 'json':
        filepath = os.path.join(base_dir, 'products.json')
        data = read_json_file(filepath)
    else:  # csv
        filepath = os.path.join(base_dir, 'products.csv')
        data = read_csv_file(filepath)

    # Handle file read errors
    if data is None:
        return render_template('product_display.html',
                               error="Error reading data file")

    # Filter by id if provided
    if product_id is not None:
        try:
            pid = int(product_id)
            filtered = [p for p in data if p.get('id') == pid]
            if not filtered:
                return render_template('product_display.html',
                                       error="Product not found")
            data = filtered
        except ValueError:
            return render_template('product_display.html',
                                   error="Invalid product id")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

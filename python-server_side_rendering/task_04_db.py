#!/usr/bin/python3
"""
Flask application that displays products from JSON, CSV, or SQLite.
Includes database creation and proper ID filtering for SQLite.
"""
import os
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def create_database():
    """Create the SQLite database and populate with sample data."""
    db_path = os.path.join(os.path.dirname(__file__), 'products.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    # Check if table is empty
    cursor.execute("SELECT COUNT(*) FROM Products")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
    conn.commit()
    conn.close()

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
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except (FileNotFoundError, KeyError):
        return None

def read_sqlite_file(db_path):
    """Read all products from SQLite database including id."""
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        products = [dict(row) for row in rows]
        conn.close()
        return products
    except sqlite3.Error:
        return None

@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQLite, optionally filtered by id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html', error="Wrong source")

    base_dir = os.path.dirname(os.path.abspath(__file__))
    data = None

    if source == 'json':
        filepath = os.path.join(base_dir, 'products.json')
        data = read_json_file(filepath)
    elif source == 'csv':
        filepath = os.path.join(base_dir, 'products.csv')
        data = read_csv_file(filepath)
    else:  # sql
        db_path = os.path.join(base_dir, 'products.db')
        create_database()
        data = read_sqlite_file(db_path)

    if data is None:
        return render_template('product_display.html', error="Error reading data file")

    if product_id is not None:
        try:
            pid = int(product_id)
            filtered = [p for p in data if p.get('id') == pid]
            if not filtered:
                return render_template('product_display.html', error="Product not found")
            data = filtered
        except ValueError:
            return render_template('product_display.html', error="Invalid product id")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=5000)

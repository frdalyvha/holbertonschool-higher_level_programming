#!/usr/bin/python3
"""
Module for consuming JSONPlaceholder API and processing data.
"""
import requests
import csv

def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print titles."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """Fetch posts and save id, title, body into a CSV file."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        data = [{'id': p['id'], 'title': p['title'], 'body': p['body']} for p in posts]
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data)

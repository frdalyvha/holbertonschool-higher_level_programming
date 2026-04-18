#!/usr/bin/python3
"""Sends a POST request with a letter to search_user API and displays result."""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': q}
    r = requests.post(url, data=data)
    try:
        json_response = r.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

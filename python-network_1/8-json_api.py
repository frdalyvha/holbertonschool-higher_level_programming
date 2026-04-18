#!/usr/bin/python3
"""Sends POST request with letter to search_user API."""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': q}
    r = requests.post(url, data=data)
    try:
        json_resp = r.json()
        if json_resp:
            print("[{}] {}".format(
                json_resp.get('id'), json_resp.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

#!/usr/bin/python3
"""Sends a POST request with email parameter and displays response body."""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    r = requests.post(url, data=data)
    print(r.text)

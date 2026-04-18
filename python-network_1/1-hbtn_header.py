#!/usr/bin/python3
"""
Module that fetches a URL and displays the value of X-Request-Id header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header_value = response.headers.get('X-Request-Id')
        print(header_value)

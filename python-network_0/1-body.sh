#!/bin/bash
# Sends a GET request to a URL and displays the body of the response (following redirects)
curl -s -L "$1"

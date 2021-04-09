#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8). (You have to manage
urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP
status code
Using the requests library
"""
import requests
from sys import argv

if __name__ == '__main__':

    url = argv[1]
    r = requests.get(url)
    rstat = r.status_code

    if rstat >= 400:
        print("Error code: {}".format(rstat))
    else:
        print(r.content.decode('utf-8'))

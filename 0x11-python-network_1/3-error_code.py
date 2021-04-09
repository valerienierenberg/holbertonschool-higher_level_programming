#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8). (You have to manage
urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP
status code
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == '__main__':

    url = argv[1]

    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.status))

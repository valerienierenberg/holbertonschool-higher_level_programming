#!/usr/bin/python3
""" Python  script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8) """
import urllib.request
import urllib.parse
from sys import argv

url = argv[1]
email = argv[2]

params = urllib.parse.urlencode({'email': email})
params = params.encode('ascii')
req = urllib.request.Request(url, params) 
with urllib.request.urlopen(req) as response:
    html = response.read()
    print(html.decode('utf-8'))

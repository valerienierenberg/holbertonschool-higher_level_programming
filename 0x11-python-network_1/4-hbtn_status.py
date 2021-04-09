#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
using the package requests """
import requests

r = requests.get('https://intranet.hbtn.io/status')

print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.content.decode('utf-8')))

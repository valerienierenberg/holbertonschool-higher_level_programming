#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv
from pprint import pprint


if __name__ == '__main__':

    username = argv[1]
    password = argv[2]

    r = requests.get('https://api.github.com/user', auth=(username,
                                                          password)).json()
    if 'id' in r:
        print(r['id'])
    else:
        print('None')

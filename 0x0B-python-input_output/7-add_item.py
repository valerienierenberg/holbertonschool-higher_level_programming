#!/usr/bin/python3
""" This module contains a script that adds all arguments to a Python list,
    and then saves them to a file """


import json
from sys import argv


save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    newlist = load_json(filename)
except (ValueError, FileNotFoundError):
    newlist = []

newlist = newlist + argv[1:]
save_json(newlist, filename)

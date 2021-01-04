#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        funcresult = fct(*args)
        return funcresult
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None

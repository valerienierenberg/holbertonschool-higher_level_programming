#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        funcresult = fct(*args)
        return funcresult
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None

# Function that executes a function safely.
# import sys module in order to print to stderr file
# try: set result of function 'fct' to variable 'funcresult'
#      return that result
# except: if anything went wrong while running function 'fct'...
# ...print error argument to stderr, and return None

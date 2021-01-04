#!/usr/bin/python3
def safe_print_division(a, b):
    x = 0
    try:
        x = (a) / (b)
        return x
    except ZeroDivisionError:
        x = None
        return None
    finally:
        print("Inside result: {}".format(x))

# Function that divides 2 integers and prints the result.
# initialize result (x) to 0
# try: set x to the result of 'a' divided by 'b'
# (return result of division)
# except: if there is a zerodivisionerror, set x to None and return None
# finally: print the result of division

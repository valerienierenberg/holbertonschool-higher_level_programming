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

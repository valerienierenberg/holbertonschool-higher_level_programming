#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for x in my_list[:x]:
            print("{}".format(my_list[x - 1]), end="")
        print()
    except IndexError:
        print()
    finally:
        return x

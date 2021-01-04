#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end="")
            a += 1
        except (ValueError, TypeError):
            y += 1
            continue
    print("")
    return(a)

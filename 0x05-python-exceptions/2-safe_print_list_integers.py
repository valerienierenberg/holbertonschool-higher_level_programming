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

# Function that prints the fist x elements of a list and only integers.
# a = counter variable to keep count correct, will be returned
# for loop iterates through list to index x
# try: print the value if an integer, increment i/count
# except: value is NOT an int, increment INDEX to skip str element...
# ...then 'continue' iterating through index until x

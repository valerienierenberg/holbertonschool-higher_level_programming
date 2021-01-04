#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for y in range(x):
        try:
            print("{}".format(my_list[y]), end="")
            a += 1
        except IndexError:
            break
    print("")
    return(a)


# --gives correct output--
# def safe_print_list(my_list=[], x=0):
#    try:
#        for x in my_list[:x]:
#            print("{}".format(my_list[x - 1]), end="")
#        print()
#    except IndexError:
#        print()
#    finally:
#        return x
#
# Function that prints x elements of a list
# i = counter variable to keep count correct, will be returned
# for loop iterates through list to index x
# print value of each element
# add to count only if index doesn't exceed length of list

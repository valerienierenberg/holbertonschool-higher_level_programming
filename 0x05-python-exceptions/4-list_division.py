#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for y in range(list_length):
        try:
            my_list_3.append(my_list_1[y] / my_list_2[y])
        except ZeroDivisionError:
            my_list_3.append(0)
            print("division by 0")
        except TypeError:
            my_list_3.append(0)
            print("wrong type")
        except IndexError:
            my_list_3.append(0)
            print("out of range")
        finally:
            pass

    return (my_list_3)

# make an empty list called 'my_list_3'
# for loop iterates through length of lists
# try: append the result of division of corresponding elements of lists...
# ...to the new list my_list_3
# for all excepts: append 0 to new list because division was unsuccessful
# (as specified in task requirements)
# return new list

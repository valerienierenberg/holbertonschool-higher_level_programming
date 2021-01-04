#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for y in range(0, list_length):
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

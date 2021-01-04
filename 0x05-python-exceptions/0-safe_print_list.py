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

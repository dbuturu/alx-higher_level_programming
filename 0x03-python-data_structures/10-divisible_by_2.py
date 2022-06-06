#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    evens = []
    for int in my_list:
        if int % 2 == 0:
            evens.append(True)
        else:
            evens.append(False)

    return evens

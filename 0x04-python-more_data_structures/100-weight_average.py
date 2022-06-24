#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0
    avg = size = 0
    for x, y in my_list:
        avg += (x * y)
        size += y
    return avg / size

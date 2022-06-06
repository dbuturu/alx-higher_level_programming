#!/usr/bin/python3
def no_c(my_string):
    copy = "".join([string for string in my_string if string != 'c' and string != 'C'])
    return copy

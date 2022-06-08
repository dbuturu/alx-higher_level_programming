#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [int if int != search else replace for int in my_list]

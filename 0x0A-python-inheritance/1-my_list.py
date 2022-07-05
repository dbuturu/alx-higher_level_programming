#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """MyList class"""

    def __init__(self):
        """init function"""
        super().__init__()

    def print_sorted(self):
        """print_sorted function"""
        print(sorted(self))

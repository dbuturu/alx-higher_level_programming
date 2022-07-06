#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    """MyInt class"""

    def __new__(cls, *args, **kwargs):
        """new function"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """eq function"""
        return int(self) != other

    def __ne__(self, other):
        """ne fuction"""
        return int(self) == other

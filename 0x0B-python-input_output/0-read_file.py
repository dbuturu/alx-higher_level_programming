#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """read_file function"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")

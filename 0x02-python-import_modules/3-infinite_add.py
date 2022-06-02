#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    total = 0
    for i, arg in enumerate(argv):
        if i == 0:
            continue
        total += int(arg)

    print("{:d}".format(total))

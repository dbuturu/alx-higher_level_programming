#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    amount = "argument"

    if len(argv) > 2 or len(argv) == 1:
        amount += "s"

    if len(argv) == 1:
        amount += "."
    else:
        amount += ":"

    print("{:d} {:s}".format(len(argv) - 1, amount))

    for i in range(1, len(argv)):
        print("{:d}: {:s}".format(i, argv[i]))

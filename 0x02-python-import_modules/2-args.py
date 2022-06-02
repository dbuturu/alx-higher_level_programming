#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    amount = "argument"

    if len(argv) > 1 or len(argv) == 0:
        amount += "s"

    if len(argv) == 0:
        amount += "."
    else:
        amount += ":"

    print(f"{len(argv)} arguments:")
    
    for i, arg in enumerate(argv):
        if i == 0:
            continue
        print(f"{i}: {arg}")

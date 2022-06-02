#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    amount = "argument"

    if len(argv) > 2 or len(argv) == 1:
        amount += "s"

    if len(argv) == 1:
        amount += "."
    else:
        amount += ":"

    print(f"{len(argv) -1} arguments:")
    
    for i, arg in enumerate(argv):
        if i == 0:
            continue
        print(f"{i}: {arg}")

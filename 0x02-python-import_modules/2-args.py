#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    print(f"{len(argv)} arguments:")
    for i, arg in enumerate(argv):
        if i == 0:
            continue
        print(f"{i}: {arg}")

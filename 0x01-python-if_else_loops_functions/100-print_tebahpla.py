#!/usr/bin/python3
for i in range(26, 0, -1):
    x = chr(97 + (i - 1))
    char = x if i % 2 == 0 else chr(ord(x) - 32)
    print("{:s}".format(char), end="")

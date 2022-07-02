#!/usr/bin/python3
"""text indentation module"""


def text_indentation(text):
    """text_indentation function"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        line = ""
        for i in range(len(text)):
            if text[i] in ['.', ':', '?']:
                line += text[i]
                print(line.strip())
                print()
                line = ""
            else:
                line += text[i]
        print(line.strip(), end="")

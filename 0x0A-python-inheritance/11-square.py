#!/usr/bin/python3
"""Square module"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """init function"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area function"""
        return self.__size ** 2

    def __str__(self):
        """str function"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

#!/usr/bin/python3
"""Square"""


class Square:
    """Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def shape(self):
        square = []
        if self.__size == 0:
            return ""
        [square.append("\n") for y in range(0, self.__position[1])]
        for y in range(self.__size):
            [square.append(" ") for x1 in range(0, self.__position[0])]
            [square.append("#") for x2 in range(0, self.__size)]
            square.append("\n")
        square.pop(-1)
        return ''.join(square)

    def my_print(self):
        print(self.shape())

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

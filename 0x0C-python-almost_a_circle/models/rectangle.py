#!/usr/bin/python3
"""Rectangle models"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init function"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @staticmethod
    def validator(name, value):
        """validator function"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @width.setter
    def width(self, value):
        """setter of width"""
        self.validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """setter of height"""
        self.validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """setter of x"""
        self.validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """setter of y"""
        self.validator("y", value)
        self.__y = value

    def area(self):
        """area function"""
        return self.__width * self.__height

    def display(self):
        """simple display function"""
        print(
            ("\n" * self.__y) + "\n".join(
                ((" " * self.__x) + ("#" * self.__width))
                for i in range(self.__height)))

    def __str__(self):
        """str function"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """update function"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation of a Rectangle"""
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["width"] = self.width
        dictionary["height"] = self.height
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary

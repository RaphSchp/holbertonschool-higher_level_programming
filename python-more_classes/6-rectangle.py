#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ class def """
    number_of_instances = 0
    __height = 0
    __width = 0

    def __init__(self, width=0, height=0):
        """ init """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        del self
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """ str """
        if (self.height > 0) and (self.width > 0):
            for i in range(self.height):
                for j in range(self.width):
                    print("#", end="")
                if i < self.height - 1:
                    print()
        return ""

    def __repr__(self):
        """ repr """
        return f"Rectangle({self.width}, {self.height})"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """ Returns area """
        return self.height * self.width

    def perimeter(self):
        """ Returns perimeter """
        if (self.height == 0) or (self.width == 0):
            return 0
        return 2 * self.height + 2 * self.width

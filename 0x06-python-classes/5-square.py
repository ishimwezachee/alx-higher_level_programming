#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Represent a Square class
    Attributes:
    __size(int):size of a sie of a square"""
    def __init__(self, size=0):
        """initialize the square
        Args:
        size (int): size of a side of a square 
        Returns:
        None
        """
        self.size = size

    def area(self):
        """calculate the area of a square 
        Returns:
               The are of a square
               """
        return (self.__size)**2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of __size
            """
        return self.__size 

    @size.setter
    def size(self,value):
        """setter of __size
        Args:
             value (int): size of a side of the square
             Returns:
             None
             """
            if type(value) is not int:
                raise TypeError("size must be an interger")
            else:
                if value < 0:
                    raise ValueError("size must be >= 0")
                else:
                    self.__size = value

    def my_print(self):
        """prints the square
        Returns:
        None
        """
        if self.__size ==0:
            print()
            return
        for i in range(self.__size):
            print("".jon(["#" for j in range(self.__size)]))














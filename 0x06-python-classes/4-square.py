#!/usr/bin/python3
"""Define a square class"""


class Square:
    """Represent a Square"""
    
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
              size (int): the size of the new square"""

        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """return the current area of a square"""
        return(self.__size * self.__size)
    @property
    def size(self):
        """getter of __size
        Returns:
        thesize of the square
        """
        return self.__size
    @size.setter
    def size(self,value):
        """ setter of __size
        Args:
        value(int): the sive of a a size of the square
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

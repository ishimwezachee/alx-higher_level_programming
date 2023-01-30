#!/usr/bin/python3
""" Define a square class """


class Square:
    """Represent a square class"""
    def __init__(self,size=0):
        """Initialize a class square
        Args:size (int): attribute of a class square"""
        if not isinstance(size,int):
            raise TypeError("size must be an integer")
        elif size<0:
            raise ValueError("size must be >= 0")
        self__.size = size



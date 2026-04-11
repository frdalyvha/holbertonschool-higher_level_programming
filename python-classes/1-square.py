#!/usr/bin/python3
"""Module that defines a Square class with private size attribute."""


class Square:
    """Class that defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize the square with a size.

        Args:
            size: The size of the square (no type/value verification yet).
        """
        self.__size = size

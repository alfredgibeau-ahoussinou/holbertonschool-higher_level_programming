#!/usr/bin/python3
"""
This is an empty class representing the base geometry.
"""


class BaseGeometry:
    """BaseGeometry class represents a base geometry shape."""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value:- name: string- value: integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

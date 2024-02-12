#!/usr/bin/python3
class BaseGeometry:
    """
    BaseGeometry class represents a base geometry shape.
    """

    def area(self):
        """
        Calculates the area of the geometry shape.
        Raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

# A python script that a has base class Shape with a method area() and derived
# classes Rectangle and Circle, each overriding the area() method to calculate
# their respective areas.

import math


class Shape:
    def area(self):
        """
            simply raises a NotImplementedError, indicating that derived 
            classes need to override this method.
            """
        raise NotImplementedError('Derived class need to override this method')


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates the area of a circle."""
        solution = math.pi * self.radius ** 2
        return solution

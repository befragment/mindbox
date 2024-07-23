from abc import ABC
import math


class Shape(ABC):
    def area(self):
        raise NotImplementedError("You cannot create instance of abstract class")


class Circle(Shape):
    def __init__(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            raise ValueError("Radius of circle must be positive")

    def area(self):
        return math.pi * self._radius ** 2
    

class Triangle(Shape):
    def __init__(self, a, b, c):
        if a > 0 and b > 0 and c > 0:
            self._a = a
            self._b = b
            self._c = c
        else:
            raise ValueError("Sides of triangle must be positive!")

    def area(self):
        p = (self._a + self._b + self._c) / 2
        return math.sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))
    
    def is_right(self):
        sorted_sides = sorted([self._a, self._b, self._c])
        return sorted_sides[0] ** 2 + sorted_sides[1] ** 2 == sorted_sides[2] ** 2


def calculate_area(shape):
    if not isinstance(shape, Shape):
        raise TypeError("Shape must be an instance of Shape class")
    return shape.area()





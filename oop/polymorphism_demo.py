""" Demonstrates polymorphism and method overriding with shape, rectangle, and Circle classes """

import math

#Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method")
    
# Rectangle class (inherits shape)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
#Circle class inherits shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return  math.pi * (self.radius ** 2)
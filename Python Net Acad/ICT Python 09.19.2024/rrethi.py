# Write a  Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math

class Circle:
    def __init__(self,rreze) -> None:
        self.r = rreze

    def area(self):
        return math.pi * self.r ** 2
    
    def perimeter(self):
        return 2*math.pi*self.r
    
circle1 = Circle(5)

print("Perimetri: ", circle1.perimeter())
print("Siperfaqja: ", circle1.area())
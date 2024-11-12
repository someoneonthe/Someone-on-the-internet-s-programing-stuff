﻿class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length # self.width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width
    
    
    
    
length = int(input("Enter length: "))
width = int(input("Enter width: " ))
r = Rectangle(length, width)
print("Area", r.area())
print("perimeter:", r.perimeter())
r.length *= 2
print("Length * 2:" , r.length)

input()
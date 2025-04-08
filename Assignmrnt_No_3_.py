"""
Q# 01 Write a program that calculates the sum, difference, product, and average of three numbers
"""

a = 10
b = 20
c = 30

print(a+b+c)
print(a-b-c)
print(a*b*c)
print(a+b+c/3)



"""Q# 02 Write Python code to calculate the area of the following shapes
*   Area=0.5​×base×height
*   Area=sidexside
*   Area=π×radius2
*   Area=length×width
"""

import math

# Area Of Triangle
def area_of_triangle(base=2, height=6):
    return 0.5 * base * height

print("area_of_triangle:")
print(area_of_triangle())

# Area Of Squre
def area_of_square(side=5):
    return side * side

print("area_of_square:")
print(area_of_square())

# Area Of Circle:
def area_of_circle(radius=2):
    return math.pi * radius **2

print("area_of_circle:")
print(area_of_circle())

# Area Of Rectangle
def area_of_rectangle(length=3, width=6):
    return length * width

print("area_of_rectangle:")
print(area_of_rectangle())




"""Q# 03 Write a program to swap values of two variables"""

# define variables
a = 5
b = 10

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swap the values
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

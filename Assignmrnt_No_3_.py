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

base = 2
height = 6
side = 5
radius = 2
length = 3
width = 6

print("Area of Triangle:")
print(0.5 * base * height)

print("Area of Squre:")
print(side * side)

print("Area of Circle")
print(3.14 * radius * radius)

print("Area of Rectangle")
print(length * width)



"""Q# 03 Write a program to swap values of two variables"""

a = 5
b = 10

print("a =", a)
print("b =", b)

print("Swapping Values:")

a = b  
b = 5

print("a =", a)
print("b =", b)

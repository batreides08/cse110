import math

#AREA OF A SQUARE
length_square = float(input("What is the length of a side of the square? "))
area_square = length_square ** 2
print(f"The area of the square is {area_square}")

#AREA OF A RECTANGLE
length_rectangle = float(input("What is the length of the rectangle? " ))
width_rectangle = float(input("What is the width of the rectangle? " ))
area_rectangle = length_rectangle * width_rectangle
print(f"The area of the rectangle is {area_rectangle}")

#AREA OF A CIRCLE
radius = float(input("What is the radius of the circle? " ))
area_circle = math.pi * (radius ** 2)
print(f"The area of the circle is {area_circle:.1f}")









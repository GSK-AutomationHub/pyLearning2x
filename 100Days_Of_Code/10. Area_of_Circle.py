# write python program to calculate area of circle. Take radius input from user
import math

radius = float(input("Enter Radius of Circle\n"))
pi = round(math.pi, 2)
print(f"math.pi value is {math.pi}, whereas pi value is {pi}")
area_of_circle = round((pi * pow(radius, 2)), 2)
print(f"Area of circe for given radius is {area_of_circle}")

square_root = round((pow(radius,1/2)), 4)
cube_root = round((pow(radius,1/3)), 4)
print(square_root, cube_root)

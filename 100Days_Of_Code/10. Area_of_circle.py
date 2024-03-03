# write python program to calculate area of circle. Take radius input from user

radius = float(input("Enter Radius of Circle\n"))
pi = 3.14
area_of_circle = round((pi * pow(radius, 2)), 2)
print(f"Area of circe for given radius is {area_of_circle}")

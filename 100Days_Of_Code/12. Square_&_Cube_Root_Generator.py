# calculate & print square and cube root of given number
import math

number = int(input("Enter the number\n"))
# square_root = round((pow(number,1/2)), 4)
square_root = math.sqrt(number)
# cube_root = round((pow(number,1/3)), 4)
cube_root = math.cbrt(number)
print(f"square root of given number is {square_root} and cube root is {cube_root}")
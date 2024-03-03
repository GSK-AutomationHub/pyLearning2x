# calculate & print square and cube of given number
number = int(input("Enter the number\n"))
# number_square = number ** 2
number_square = pow(number, 2)
# number_cube = number_square * number
number_cube = pow(number, 3)
print(f"square of given number is {number_square} and number cube is {number_cube} ")

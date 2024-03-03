# PEMDAS LR
# # Parenthesis - Exponent - Multiplication - Division - Addition - Subtraction in order Left to right
# () --> ** --> *,/ --> +,- L --> R

# Problem statement
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# NOTE: You should convert the bmi to a whole number and print out a whole number
# Example Input 1
# height - 1.75 , weight - 80
# So, BMI = 80 ÷ (1.75 x 1.75) = 26.122448979591837

height = float(input("enter your height in meters\n"))
weight = float(input("enter your weight in kilograms\n"))
# BMI = int(weight / (height ** 2))
BMI = int(weight / (pow(height,2)))
print("Your BMI Calculated is ", BMI)

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Equal to or over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.

height = float(input("enter your height in meters\n"))
weight = float(input("enter your weight in kilograms\n"))
# BMI = int(weight / (height ** 2))
BMI = int(weight / (pow(height, 2)))
if BMI < 18.5:
    print(f"Your BMI is {BMI},Your are Underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI},You have a Normal Weight")
elif BMI < 30:
    print(f"Your BMI is {BMI},You are Slightly Overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI},You are Obese")
else:
    print(f"Your BMI is {BMI},You are Clinically Obese")


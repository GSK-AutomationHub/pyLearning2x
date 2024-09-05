# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
# Input = 2024
# Output = Leap year

print("---------------------- Approach 1 --------------------------")

year = int(input("Please enter the year\n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Its a Leap Year")
        else:
            print("Its not a Leap Year")
    else:
        print("Its a Leap Year")
else:
    print("Its not a Leap Year")

print("---------------------- Approach 2 --------------------------")

year = int(input("Please enter the year\n"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Its a Leap Year")
else:
    print("Its not a Leap Year")

# Write a program that adds the digits in a 2 digit number. e.g.
# if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Enter two digit number\n")
print(type(two_digit_number))
first_digit=int(two_digit_number[0])
last_digit=int(two_digit_number[-1])
print("The Result of Addition is ", first_digit+ last_digit)
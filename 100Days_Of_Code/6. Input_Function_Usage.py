# Input function is used to collect user input which can be printd or assign to varibale
# for further usage in code. Imp - User input entered replaces complete input function.

# print power of numer
num_1=int(input("Enter First Number "))
num_2=int(input("Enter Second Number "))
print(type(num_1))
print(type(num_2))
result = (num_1**num_2)
print("Result of Power Calculation is ", result)

# print length of string
print(len(input("Enter your name ")))
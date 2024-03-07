number = int(input("Enter the number\n"))
count = number
i= count
fact = 1

print(f"-----------{number}! using while loop ----------")
while count > 0:
    fact *= count
    count -=1
print(f"{number}! is {fact}")

print(f"-----------{number}! using for loop ----------")
for i in range(i,1):
    fact *=  i
    i -=1
print(f"{number}! is {fact}")
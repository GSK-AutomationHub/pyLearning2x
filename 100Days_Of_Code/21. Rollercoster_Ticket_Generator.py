#write code to generate roller coaster ticker based on user height and age
#to enter, height must greater than or equal to 120 cms
#ride charges should be $5 below 12 year old, $7 between 12 to 18 and $12 above 18 years

print("Welcome to Roller coaster !!!")
height = int(input("Enter your height in cms\n"))
if height >= 120:
    print("You are eligible to take Roller coaster Ride !!")
    age = int(input("Please submit your current age\n"))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay &7")
    else:
        print("Please pay $12")
else:
    print("You are not eligible fo roller coaster ride as of now")

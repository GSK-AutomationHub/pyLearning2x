# tip calculator
print("Welcome to Tip Calculator !!!")
bill = float(input("Enter total bill amount\n"))
tip = int(input("Enter percentage tip you would like to give? 10, 12 or 15\n"))
count = 1
while count < 3:
    if tip != (10 or 12 or 15):
        count += 1
        if count == 3:
            exit()
        else:
            tip_percentage = int(input("please enter correct tip option out of 10, 12 or 15\n"))
    else:
        break
people = int(input("Enter how may people to split the bill?\n"))
bill_with_tip = bill + (bill * (tip / 100))
bill_per_person = bill_with_tip / people
# bill_per_person = round(bill_per_person, 2)
bill_per_person = "{:.2f}".format(round(bill_per_person, 2))
print(f"Each person should pay: ${bill_per_person}")

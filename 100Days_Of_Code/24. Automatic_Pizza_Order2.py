print("Thank you for choosing Delicious Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L\n")
if size not in ['S', 'M', 'L']:
    print("Invalid Option")
    exit()
add_pepperoni = input("Do you want pepperoni? Y or N\n")
if add_pepperoni not in ['Y', 'N']:
    print("Invalid Option")
    exit()
extra_cheese = input("Do you want extra cheese? Y or N\n")
if extra_cheese not in ['Y', 'N']:
    print("Invalid Option")
    exit()
bill = 0
if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
else:
    bill = 25
if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
if extra_cheese == 'Y':
    bill += 1
print(f"Your final bill is: ${bill}")

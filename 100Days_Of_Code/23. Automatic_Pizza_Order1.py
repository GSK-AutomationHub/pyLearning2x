# Delicious Pizza! build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small pizza (S): $15, Medium pizza (M): $20, Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1
# Example Input - L, Y, N
# Example Output- Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.

print("Thank you for choosing Delicious Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M, or L\n")
if size not in ['S', 'M', 'L']:
    print("Invalid Option")
    exit()
add_pepperoni = input("Do you want pepperoni? Y or N\n")
if add_pepperoni not in ['Y','N']:
    print("Invalid Option")
    exit()
extra_cheese = input("Do you want extra cheese? Y or N\n")
if extra_cheese not in ['Y','N']:
    print("Invalid Option")
    exit()

if size == 'S':
    bill = 15
    if add_pepperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += 1
elif size == 'M':
    bill = 20
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
elif size == 'L':
    bill = 25
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
print("Thank you for choosing Delicious Pizza Deliveries")
print(f"Your final bill is: ${bill}")

# write program to calculate and display score grade

score = int(input("Enter the score\n"))
# if 90 <= score <= 100:
if score >= 90 and score <=100:
    print("A Garde")
elif score>=80 and score <=89:
    print("B Garde")
elif score>=70 and score <=79:
    print("C Garde")
elif score>=60 and score <=69:
    print("D Garde")
elif score>=0 and score <=59:
    print("E Garde")
else:
    print("Invalid Score Entered")

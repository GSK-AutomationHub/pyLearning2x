# Band Name Generator prog example of string concatenation

print("Hey ..Welcome to Band Name Generator")

City = input("What's name of the city you grew up in?\n")
# print("City you entered", City)

Pet = input("What's name of your pretty pet?\n")
# print("Pet name you entered", Pet)

# Band_Name_Suggestion = '"{} {}"'.format(City,Pet)
Band_Name_Suggestion = f'"{City} {Pet}"'

print("Here is Band Name you can think of", Band_Name_Suggestion)

# Learning python strings functions continued...
message = 'Hello world'

# function to print in upper case
print(message.upper())

# function to print in lower case
print(message.lower())

# function to count recurrence of character/word in string
print(message.count('world'), message.count('universe'), message.count('o'))

# function to find index of character/word in string
print(message.find('world'), message.find('o'))

# find function return index -1, if character/word not present it string
print(message.find('universe'))
# Learning python strings functions
message = 'Hello world'

# dir function gives list of functions available for string literal
print(dir(message))

# help function
print(help(str))
print(help(str.find))

# len gives length of the string
print(len(message))

# we can get character at specified index starting from 0, last index is always length-1
print(message[0], message[10])

# we can print part of string using index range, it called slicing, it prints slice till last index-1
print(message[0:5], message[6:11])

# we can print string slice w/o mentioning 1st or last index, 0th & last index consider in that case
print(message[:5], message[6:])


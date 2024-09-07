# Learning python strings functions
#  - strings in pythn are arrays, so it uses indexes for slicing & get substring
#  - slicing syntax [start_index : end_index : steps]
#  - slicing function always excludes last i.e. ending index while returning substring,

message = 'Hello world'
str = 'this is sample string'

# dir function gives list of functions available for string literal
print(dir(message))

# help function
#print(help(str))
#print(help(str.find))

# len gives length of the string
print(len(message))

# we can get character at specified index starting from 0, last index is always length-1
print(message[0], message[10])

# we can print part of string using index range, it called slicing, it prints slice till last index-1
print(message[0:5], message[6:11])

# it will return substring from 0th till 6th index ---> 'this is'
print(str[0:7])

# we can print string slice w/o mentioning 1st or last index, 0th & last index consider in that case
print(message[:5], message[6:])

# string with reserve index
print(message[-6:-1])
print(message[-6:])

# usage of step in index

#str [0:-1:1] --> it wil print original string
print(message [0: -1: 1])

#str [0:-1:2] --> it wil print sub string omitting alternate charac in string
print(message [0: -1: 2])

#str [0:-1:3] --> it wil print sub string omitting alternate 2 charac in string
print(message [0: -1: 3])


# reserve of string
r_message = message[: : -1]
# it will reverse string as it return substring by stepping each charac in desc way
print(r_message)

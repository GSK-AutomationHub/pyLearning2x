# Learning List

courses = ['History', 'CompSci', 'Math', 'English']

# to print various functions available for list
print(dir(list))
# print(help(list.sort()))

# to print length of list
print(len(courses))

# to print value at specific index in list,index starts from 0,
print(courses[0])
print(courses[3])

# listname [-1] always print last index value in list
print(courses[-1])

# index out of rage error for incorrect index
#print(courses[4])

# slicing of list, last index is exclusive, first & last index ll be autofill as 0 & -1 if not mentioned
print(courses[0:2])
print(courses[1:4])
print(courses[:3])
print(courses[1:])
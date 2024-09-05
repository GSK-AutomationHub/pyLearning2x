# Learning looping & string/list conversions

courses = ['Physics', 'History', 'CompSci', 'Geography', 'Math']
num = [1, 3, 6, 5, 9, 0]

# for each in python
for course in courses:
    print(course)

# enumerate function returns list value with index
for index,course in enumerate(courses):
    print(index,course)

# enumerate function with customized start value
for index,course in enumerate(courses, start=1):
    print(index,course)

# join function used for converting list to string , it requires to specify seperator
courses_str = ', '.join(courses)
print(courses_str)

# split function used for converting string to list , it requires to specify seperator
back_to_list = courses_str.split(', ')
print(back_to_list)
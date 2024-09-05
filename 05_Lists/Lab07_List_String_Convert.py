# Learning string/list conversions

courses = ['Physics', 'History', 'CompSci', 'Geography', 'Math']

# list to string --> join function used for converting list to string, it requires to specify seperator
courses_str = ', '.join(courses)
print(courses_str)

# string to list --> split function used for converting string to list , it requires to specify seperator
back_to_list = courses_str.split(', ')
print(back_to_list)
# Learning List methods

courses = ['History', 'CompSci', 'Math', 'English']

# append method used to add value at last index of list
courses.append('Art')
print(courses)

# pop method used to remove value at last index of list, it returns the removed value
removed_courses = courses.pop()
print(courses)
print(removed_courses)

# insert method used to add value at specific index of list
courses.insert(0, 'Physics')
print(courses)
courses.insert(3, 'Geography')
print(courses)

# Adding / removing list into other list
new_courses = ['SocialSci', 'PT']
print(new_courses)

courses.append(new_courses)
print(courses)

courses.pop()
print(courses)

courses.insert(0, new_courses)
print(courses)

courses.remove(new_courses)
print(courses)

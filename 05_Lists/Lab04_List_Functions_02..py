# Learning List methods continued ..

courses = ['Physics', 'History', 'CompSci', 'Geography', 'Math']

# extend method used to add values of list into other list
new_courses = ['SocialSci', 'PT']

courses.extend(new_courses)
print(courses)

# reverse method is used to reverse the sequence/index of curses in list
courses.reverse()
print(courses)

# sort method used to sort the list in ascending manner
num = [1, 5, 6, 9, 3, 2]
courses.sort()
num.sort()
print(courses)
print(num)

# sort method using reverse=True for sorting the list in descending manner
courses.sort(reverse=True)
num.sort(reverse=True)
print(courses)
print(num)

# sorted function used to get sorted version of list without altering original list
sorted_courses = sorted(courses)
print(courses)
print(sorted_courses)

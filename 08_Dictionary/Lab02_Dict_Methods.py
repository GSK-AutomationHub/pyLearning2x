student_dict = {"Roll_No": 12,
                "Name": "James Clear",
                "Class": 10,
                "CAGR": 90.06,
                "isMonitor": True
                }

# Accessing item from Dictionary
print(student_dict)
x, y = student_dict["Name"], student_dict["CAGR"]
print(f'student name is {x} & the CAGR is {y}')

# get() : returns value of specified key
print(student_dict.get("Name"))

# Adding item to Dictionary
student_dict["subject"] = ["Science", "Maths", "English"]
print(student_dict)

# update() : returns list of tuples having key values pairs from dict
student_dict.update({"Tutor" : "Mr. Jones"})
print(student_dict)

# Removing item from Dictionary
student_dict.pop("subject")
print(student_dict)

# popitem () : removes key value a pair of last index key
student_dict.popitem()
print(student_dict)

# key() : returns list of keys in dict
print(student_dict.keys())

# values() : returns list of values in dict
print(student_dict.values())
print(type(student_dict.values()))

# item() : returns list of tuples having key values pairs from dict
print(student_dict.items())

# copy() : create copy of specified dict
student_dict.update({'isMonitor': True , "Tutor" : "Mr. Jones"})
student_dict_copy = student_dict.copy()
print(student_dict_copy)

# clear() : clear the dict & returns None
print(student_dict_copy.clear())
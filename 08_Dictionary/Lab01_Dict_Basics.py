"""
Dictionary {}
- Dictionary is one of the COLLECTION & it saves values of same or different DT
- Dictionary stores the item in key value pair separated by :
   - Key could be Int, String
   - value could be Int, String, Float, Boolean, Array, Function
- Dictionary is ORDERED & follows INDEXATION
- One can add, remove, append, pop values at specific index thus Dictionary is MUTABLE
- Dictionary accepts NO DUPLICATE values
"""

# Defining Dictionary

# empty dictionary
demo_dict = {}
print(demo_dict)

# - Dictionary stores the item in key value pair separated by :
#    - Key could be Int, String
#    - value could be Int, String, Float, Boolean, Array, Function
# student record dictionary

student_dict = {"Roll_No": 12,
                "Name": "James Clear",
                "Class": 10,
                "CAGR": 90.06,
                "isMonitor": True
                }

print(type(student_dict))

print(student_dict)

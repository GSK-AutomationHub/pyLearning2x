'''
Tuple Methods -
 - Methods not supported - since Tuples are immutable it does not support functions like append, add, remov, pop etc.
 - Methods supported - len, count, index
'''

demo_tuple1 = (1,2,3,4,5,6)
demo_tuple2 = ("Pune", "Mumbai", "Pune" ,"Nashik", "Kolhapur", "Satara")

# count() : returns n of time item appears in tuple
print(demo_tuple2.count("Pune"))

# index() : return index of ele in tuple
print(demo_tuple2.index("Kolhapur"))

# Tuple support indexing so return value at particular index & supports index range
print(demo_tuple2[3])
print(demo_tuple2[:4])
print(demo_tuple2[3:])
print(demo_tuple2[: :-1])
print(demo_tuple2[: :3])

# Iterating thr tuples
for city in demo_tuple2:
    print(city)

# joining two or more tuples
joined_tuple = demo_tuple1 + demo_tuple2
print(joined_tuple)





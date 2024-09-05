'''
Set {}
- Set is one of the COLLECTION & it saves values of same or different DT
- Set do not store the item in sequence & thus it is UNORDERED & do not follow indexation
- One can add, remove, append, pop values at specific index thus Set is MUTABLE
- Set accept NO DUPLICATE values

Set Support Membership testing (in, not in operators) & to eliminate duplicate values

Set Methods - set(), len, add, remove, discard, pop, clear, union, update, intersection, update_intersection
              difference, symmetric_difference, symmetric_difference_update, issubset, issuperset
'''

cities = set(('pune','mumbai','banglore','hyderabad'))
print(cities)

# Membership Operators
print('pune' in cities)
print('chennai' not in cities)

# add() : add element in set
cities.add('chennai')
print(cities)

# remove() : removes ele from set
cities.remove('hyderabad')
print(cities)

# discard() : removes ele from set
cities.discard('chennai')
print(cities)

# pop() : remove ele at specified index else last index from set
cities = set(('pune','mumbai','banglore','hyderabad','chennai'))
print(cities)
cities.pop()

india_cities = set(('pune','mumbai','bangalore','goa','hyderabad','chennai'))
us_cities = {'new york', 'boston', 'huston', 'california','pune','mumbai','bangalore'}

# union() : add two sets by removing duplicate ele / values & return new set
indo_us_cities = india_cities.union(us_cities)
print(indo_us_cities)

# update() : modify sets values by ignoring duplicate ele / values & does not return new set
# india_cities.update(us_cities)
# print(india_cities)

# intersection() : return intersection i.e. duplicate or common ele / values of two set, & return new set
indo_us_intersection = india_cities.intersection(us_cities)
print(indo_us_intersection)

# update_intersection() : return intersection i.e. duplicate or common ele / values of two set, does not return new set
# india_cities.intersection_update(us_cities)
# print(india_cities)

# symmetric_difference() : return unique ele / values of two set, i.e. eliminate duplicates & return new set
sym_diff_cities = india_cities.symmetric_difference(us_cities)
print(sym_diff_cities)

# symmetric_difference_update(): return unique ele / values of two set, i.e. eliminate duplicates & does not return new set
# india_cities.symmetric_difference_update(us_cities)
# print(india_cities)

# difference() :
diff = india_cities.difference(us_cities)
print(diff)

india_cities = set(('pune','mumbai','bangalore'))
us_cities = {'new york', 'boston', 'huston', 'california','pune','mumbai','bangalore'}

# issubset() : return boolean T/F id set is subset of another set
print(india_cities.issubset(us_cities))

# issuperset() : return boolean T/F id set is superset of another set
print(india_cities.issuperset(us_cities))
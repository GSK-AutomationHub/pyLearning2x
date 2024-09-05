greeting = 'Hello'
name = 'Ganesh'
# String concatenation
print(greeting + ', ' + name + '. Welcome!')

# formatted string with placeholders
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# f strings
message = f'{greeting}, {name}. Welcome!'
print(message)

message = '%s, %s. Welcome!' % (greeting, name)
print(message)

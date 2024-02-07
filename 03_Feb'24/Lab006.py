# Learning python strings functions continued...
message = 'Hello world'

# replace function has string return type so need to collect in variable
message = message.replace('world', 'Universe')
print(message)

greeting = 'Hello'
name = 'Ganesh'
# String concatenation
print(greeting + ', ' + name + '. Welcome!')

# formatted string with placeholders
message = '{}, {}. Welcome!'.format(greeting,name)
print(message)

# f strings
message = f'{greeting}, {name}. Welcome!'
print(message)
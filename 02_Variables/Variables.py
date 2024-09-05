import keyword

# Pyhon variable rules

# variable can start with letter or underscore
_var = 'test string'
print(_var)

# variable should not start with number
#7_var = 'test string'
# print(7_var)

# variable should not use reserve keywords
# return = 'Hellow World'
# print(return)

# method to get reserve keywords
print(keyword.kwlist)
print(keyword.iskeyword('lambda'))
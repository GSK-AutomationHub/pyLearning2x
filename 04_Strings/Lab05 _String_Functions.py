#  python strings functions ...
test_str = 'this is a python string tutorial'
message = 'Hello world'

# dir() : returns functions available for string
print(dir(test_str))

# len() : return length of str/list
print(len(test_str))

# str() : convert the value in string
x = 123
y = str(x)
print(type(y))

# find(): find & return index of substring / charac
print(test_str.find("python"))
print(message.find('world'), message.find('o'))
# find function return index -1, if character/word not present it string
print(message.find('universe'))

# index () : return index of substring / charac
print(test_str.index("tutorial"))

# upper() : function to print in upper case
print(message.upper())

# lower() : function to print in lower case
print(message.lower())

# count() : function to count recurrence of character/word in string
print(message.count('world'), message.count('universe'), message.count('o'))


# - isupper() : return boolean result based on text upper or not
case_check = 'hello world'
print(case_check.isupper())

# - islower() : return boolean result based on text upper or not
print(case_check.islower())

# split(seperator, maxsplit) : split string at specified seperator & return list from left
print(test_str.split())

# rsplit(seperator, maxsplit) : split string at specified seperator & return list from right
print(test_str.rsplit())

# strip() : returns trimmed version of string
txt = '    !!rbr!! This is sample statement  '
txt = txt.strip(" !!rbr!! ")
print(txt)

# rstrip() : removes  ending space / charac
txt = '    This is sample statement !!rbr!!   '
txt = txt.rstrip(" !!rbr!! ")
print(txt)

# lstrip() : removing starting space / charac
txt = '    !!rbr!! This is sample statement  '
txt = txt.lstrip(" !!rbr!! ")
print(txt)

# replace (old,new,count) : replace old phrase with new one """
txt = 'This is sample statement'
text = txt.replace('statement', 'text')
print(text)








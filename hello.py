""" print("hello world")
print(10+20)
a=20
b=30
result=a+b
print(result)

print("memory ID :",id(result))
print("data type :",type(result))
print(dir(result))
sample_str = "this is a string"
print(sample_str, type(sample_str))"""
# print(dir(sample_str))

# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

""" print(sample_str.capitalize())  # converts first letter into capital

print(sample_str.casefold())    #converts everything iinto small case
# print(sample_str.center())
print(sample_str.split(' ')) """   # convert a string into words using space as delimeter


""" sample_str = "Hello,name is pavan"

print(sample_str.index('H'))
print(sample_str.index('o')) """

# python supports negative indexing

""" sample_char = sample_str[-1]
print(sample_char)
print(sample_str.find('p')) """



# list


""" l = [1,2,3,"abc",True,[1,2,3,"abc",True]]

print(l)

print(l,type(l))

print(l[2])
print(l[5][4])

print(dir(l)) """

"""
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

"""

l = [1,2,3,"abc",True,[1,2,3,"abc",True]]

l.append(True)

print(l)

l.append([1,2,3,"abc",True])

print(l)                         #using append method of list data type we can add objects to the list,where we can add multiple values

l1 = l.append([1,2,3,"abc",True])

print(l1)  # it will return none, because it is inplace operation

l.insert(0,"abc")    #using insert we can place a value in desired position

print(l)

l.insert(3,8)

print(l)

l.extend([8,7,5])   # extend will not add entire list to the list it add each one individually

print(l)

l2 = [9,6,3]
# l2.sort()
l3 = sorted(l2)
print(l3)









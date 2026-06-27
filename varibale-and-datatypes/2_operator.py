# Arithmetic Operators =

a = 10
b = 3

print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)


# Comparison Operators =

a = 10
b = 20

print(a < b)
print(a > b)
print(a == b)


c = 10
c += 2
print(c)


x = True
y = False
z = True

print(not x)
print(y or z)
print(not x or y)


meaning = 8
print(" ")

# if meaning > 10:
#     print('today')

# else:
#     print('not today')

# Ternary operator
print('not today') if meaning > 10 else print('today')


# Zip = it combine two list adjacently  'or' combines elements from two or more lists position-wise into pairs (or tuples).

names = ["A", "B"]
marks = [90, 80]

print(list(zip(names, marks)))

# Enumerate = With enumerate() → index + value.

names = ["A", "B", "C"]

for item in enumerate(names):
    print(item)

# or

names = ["A", "B", "C"]

for index, name in enumerate(names):
    print(index, name)
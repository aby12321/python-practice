# variable is a box that stores information.

# Example =
name = "Abhay"
age = 22

# Data Types

#1 Integer (whole no.)
age = 22
marks = 75

#2 Float (decimal)

height = 5.8
price = 99.99

#3 String (text)

name = "Abhay"
city = "Aligarh"

#4 Boolean (true or false)

is_student = True
is_raining = False

#5 Complex

comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# How to check data types =

name = "Abhay"
age = 20
height = 5.8
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# Other ways to check data types =

pizza = str("Pepperoni")

print(type(pizza) == str)
print(isinstance(pizza, str))

decade = str(1980)

statment = "i like rock music from the " + decade + "s."
print(statment)




# multiple lines

multiline = '''
hey how are you ?

I was just checking in.
                           All good?


'''
# print(multiline)


# Escaping special character =
sentence = 'I\'m back at home!\tHey!\n\nwhere\'s this at\\located?'
# print(sentence)


# lower for small  and upper for capital.
# title make every word first alphabet capital of the sentence.

print(multiline.title())
print(multiline.replace("good","ok"))

# len for length.
# Strip = Removing Whitespace (text = "   Hello, World!   \n"
#cleaned_text = text.strip()

# print(f"Original: '{text}'")
# print(f"Stripped: '{cleaned_text}'")
# Output:

# Plaintext
# Original: '   Hello, World!  '
# Stripped: 'Hello, World!'),
# or
# Removing Specific Characters
# (text = "www.example.com"
# Remove 'w', 'c', 'o', 'm', and '.' from both ends
# cleaned_text = text.strip("wcom.")
# print(cleaned_text)
# Output:
# Plaintext
# example


# Build a menu

title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Cake".ljust(16, ".") + "$2".rjust(4))
print("Latte".ljust(16, ".") + "$4".rjust(4))
print("Tea".ljust(16, ".") + "$5".rjust(4))

print(" ")


print(name.startswith("A"))
print(name.endswith("h"))


import math
print(math.pi)
print(math.sqrt(64))
print(math.ceil(height))
print(math.floor(price))

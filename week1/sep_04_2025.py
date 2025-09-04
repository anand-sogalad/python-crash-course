"""
Creating comments in python
"""

# single line comment
# This is a comment in python :)

# Multi-line comment
# Python does not have specific syntax for multi-line comments
# but we can use triple quotes to create a multi-line string
"""
This is a multi-line comment
in python
It can span multiple lines
"""


"""Python Variables"""

# Creating variables
# python doesn't support declaring variable alone
# variable get created along with when data is assigned to it

x = 5  # integer variable
y = "Hello"  # string variable
z = 3.14  # float variable

print(x, y, z, sep=", ")  # Output: 5, Hello, 3.14


# Python is a dynamically typed langunage meaning that no type is mentioned while creating variable

a = 10  # initially a is an integer
print(a, type(a))  # Output: 10 <class 'int'>

a = "Hello"  # now a is a string
print(a, type(a))  # Output: Hello <class 'str'>


# Python also supports type casting
b = 20  # integer
print(b, type(b))  # Output: 20 <class 'int'>

b = str(b)  # type casting integer to string
print(b, type(b))  # Output: 20 <class 'str'>

b = float(b)  # type casting string to float
print(b, type(b))  # Output: 20.0 <class 'float'>


# python variable are case sensitive
# Python supports both single and double quotes for string creation
name = "John"  # valid variable
print(name)  # Output: John

Name = "John"  # valid variable
print(name, Name)  # Output: John John

# lets check the validation
print(f"Checking whether name and Name are same or not (memory): {name is Name}")


"""Variable Names"""

# variables must start with a letter or underscore (_)
# variables cannot start with a number
# variables can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# variable names are case-sensitive (age, Age and AGE are three different variables)
# variable names should not be Python keywords (like: if, else, while, for, etc.)

# Valid variable names
my_variable = 10
_variable = 20
variable1 = 30
variable_name = "Hello"

# Invalid variable names
# 1variable = 10  # starts with a number
# my-variable = 20  # contains a hyphen
# my variable = 30  # contains a space
# if = 40  # uses a Python keyword

print(
    my_variable, _variable, variable1, variable_name, sep=", "
)  # Output: 10, 20, 30, Hello

# python recommends using snake_case for variable names
my_variable_name = "John Doe"
print(my_variable_name)  # Output: John Doe


"""Multiple Variable Assignment"""

# assigning multiple values to multiple variables
a, b, c = 1, 2, 3
print(a, b, c, sep=", ")  # Output: 1, 2, 3

# assigning same value to multiple variables
x = y = z = 10
print(x, y, z, sep=", ")  # Output: 10, 10, 10

# unpacking a collection
fruits = ["apple", "banana", "cherry"]
fruit1, fruit2, fruit3 = fruits
print(fruit1, fruit2, fruit3, sep=", ")  # Output: apple, banana, cherry
# Note: number of variables must match the number of values in the collection
# otherwise it will raise a ValueError
# fruit1, fruit2 = fruits  # ValueError: too many values to unpack (expected 2)

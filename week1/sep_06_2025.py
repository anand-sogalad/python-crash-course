"""
Outputing the variables
"""

x = "Python is awesome"
print(x)

# we can also pass multiple arguments to print
x = "Python"
y = "is"
z = "awesome"
print(x, y, z, sep=" ")


"""Global Variables"""
x = "I am a global variable, defined outside a function"


def my_func():
    print(
        f"This print statement is inside the function: {x}"
    )  # Accessing the global variable inside the function


my_func()
print(f"This print statement is outside the function: {x}")

# what happens if we define a variable with the same name inside the function?
x = "I am a global variable, defined outside a function"


def my_func():
    x = "I am a local variable, defined inside the function"
    print(
        f"This print statement is inside the function: {x}"
    )  # Accessing the local variable inside the function


my_func()
print(f"This print statement is outside the function: {x}")


# create global variable insidde a function
def my_func():
    global var
    var = "I am global variable, but created inside a function"
    print(var)


my_func()
print(
    f"This print statement is outside the function: {var}"
)  # var became global variable after using global keyword inside the function


# try modifiing a global variable inside a function without using global keyword
x = "I am a global variable, defined outside a function"


def my_func():
    global x
    x = x + "I am a local variable, defined inside the function"
    print(
        f"This print statement is inside the function: {x}"
    )  # Accessing the local variable inside the function


my_func()
print(f"This print statement is outside the function: {x}")


"""Data Types in Python"""
# str, int, float, complex, list, tuple, range, dict, set, frozenset, bool, bytes, bytearray, memoryview, NoneType
a = "Hello, World!"  # str
b = 20  # int
c = 20.5  # float
d = 1j  # complex
e = ["apple", "banana", "cherry"]  # list
f = tuple(e)  # tuple
g = range(6)  # range
h = {"name": "John", "age": 36}  # dict
i = {"apple", "banana", "cherry"}  # set
j = frozenset(i)  # frozenset
k = True  # bool
l = b"Hello"  # bytes
m = bytearray(5)  # bytearray
n = memoryview(bytes(5))  # memoryview
o = None  # NoneType

for item in (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
    print(f"{item} is of type {type(item)}")

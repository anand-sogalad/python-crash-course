"""Strings in Python"""

# Strings are sequences of characters enclosed in either single or double quotes
# Strings are immunutable, meaning they cannot be changed after creation

str1 = "I am a string"
str2 = "I'm also a string"

print(str1, str2, sep="\n")


# multiline string assignment
multi_line_str = """I am crazy.
Hope you know about it.
Good for you!"""

print(multi_line_str)

# string indexing
sample_str = "I am a string"
print(
    f"First element of a 'sample_str' is {sample_str[0]}"
)  # this gets the first element of a string


# iterating through string
str_to_iterate = "You can iterate through me"
for char in str_to_iterate:
    print(char, end=" ")
print()

# how to get string length
print(f"Length of 'str_to_iterate' is {len(str_to_iterate)}")

# check if a substring present in a string
print("m" in str_to_iterate)
print("me" in str_to_iterate)
print("can i" in str_to_iterate)


"""String slicing and indexing"""

str1 = "I love python programming"

# slice is getting part of a string
print(f"first 10 chars of a string: {str1[:10]}")
print(f"Last 10 chars of a string: {str1[-10:]}")


"""Modufying strings using built-in methods"""

str1 = "I love python programming, because it's awesome"

# convert all chars to upper case
print(f"All upper case: {str1.upper()}")

# convert all to lower case
print(f"All lower case: {str1.lower()}")

# remove leading or trailing white spaces
print(f"removing leading or trailing white spaces: {'  I am creazy   '.strip()}")

# replace a string
print("I am crazy".replace("a", "ssss"))

# splitting strings that converts to list
print("I am crazy".split())


# string methods
print("i am anand".capitalize())  # Output: I am anand
print("I AM ANAND".casefold())  # Output: i am anand
print("I am anand".center(20, "-"))  # Output: ----I am anand-----
print("I am anand".count("am"))  # Output: 1
print("I am anand".encode())  # Output: b'I am anand'
print("I am anand".endswith("and"))  # Output: True
print("I am anand".find("anand"))  # Output: 5
print("I am anand".isalnum())  # Output: False
print("Iamanand".isalnum())  # Output: True
print("I am anand".isalpha())  # Output: False
print("Iamanand".isalpha())  # Output: True
print("12345".isdigit())  # Output: True
print("I am anand".islower())  # Output: True
print("I AM ANAND".isupper())  # Output: True
print("   ".isspace())  # Output: True
print("I am anand".istitle())  # Output: False
print("I Am Anand".istitle())  # Output: True
print("I am anand".join(["Hello", "World"]))  # Output: Hello
print("I am anand".lstrip("I "))  # Output: am anand
print("I am anand".rstrip("and"))  # Output: I am an
print("I am anand".partition("anand"))  # Output: ('I am ', 'anand', '')
print("I am anand".replace("anand", "crazy"))  # Output: I am crazy
print("I am anand".rfind("anand"))  # Output: 5
print("I am anand".startswith("I am"))  # Output: True
print("I am anand".swapcase())  # Output: i AM ANAND
print("I am anand".title())  # Output: I Am Anand
print("I am anand".zfill(20))  # Output: 000000000I am anand
print("I am anand".index("anand"))  # Output: 5
print("I am anand".isdecimal())  # Output: False
print("12345".isdecimal())  # Output: True
print("I am anand".isnumeric())  # Output: False
print("12345".isnumeric())  # Output: True
print("I am anand".isidentifier())  # Output: False
print("anand".isidentifier())  # Output: True
print("I am anand".maketrans("anand", "crazy"))  # Output: {97: 99, 110: 114, 100: 122}
print("I am anand".translate(str.maketrans("anand", "crazy")))  # Output: I am crzy
print("I am anand".format())  # Output: I am anand
print("I am anand".format_map({"anand": "crazy"}))  # Output: I am crazy
print("I am anand".removeprefix("I am "))  # Output: anand
print("I am anand".removesuffix("and"))  # Output: I am
print("I am anand".splitlines())  # Output: ['I am anand']

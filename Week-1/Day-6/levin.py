"""
Author = levin abraham jacob
date = 24-11-2024
description = Data Types
"""
#
int_ = 99
float_ = 3.14
bool_ = True
string_ = "Hello, World!"
print(int_, type(int_))
print(float_, type(float_))
print(bool_, type(bool_))
print(string_, type(string_))
#task 2: Perform Operations with Strings
string1 = "Python"
string2 = " is fun!"
result = string1 + string2
print(result) #concatination
rep = string1 * 3#multipies the string
print(rep)
length = len(result)
print("Length of the string:", length)

#Task 3: Boolean expressions
bool1 = (5 > 3)
bool2 = (10 == 15)

print(bool1, type(bool1))  # True
print(bool2, type(bool2))  # False

# Invert boolean value
inverted = not bool1
print(inverted, type(inverted))

# Float operations
deci = 99.99999
rounded_deci = round(deci,2)
print(f"Original value = {deci}")#value = 99.99999
print(f"Rounded value  = {rounded_deci}")#value = 100.0

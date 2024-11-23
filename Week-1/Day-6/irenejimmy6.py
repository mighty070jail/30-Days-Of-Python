'''
Author:IRENE JIMMY
Date:22-11-24
'''

#PART 1 Create Variables with Different Data Types
my_int = 10
my_float = 3.14
my_bool = True
my_string = "Hello, World!"
print(my_int, type(my_int))
print(my_float, type(my_float))
print(my_bool, type(my_bool))
print(my_string, type(my_string))

#PART2 Perform Operations with Strings
string1 = "Python"
string2 = " is fun!"
result = string1 + string2
print(result)
repeated = string1 * 3
print(repeated)
length = len(result)
print("Length of the string:", length)

#PART3 Work with Booleans
bool1 = (5 > 3)
bool2 = (10 == 15)
print(bool1, type(bool1))
print(bool2, type(bool2))
inverted = not bool1
print(inverted, type(inverted))

#PART4 Explore Floats
pi = 22 / 7
rounded_pi = round(pi, 2)
print("Original:", pi)
print("Rounded:", rounded_pi)
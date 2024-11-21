# Day-6: Explore and Practice Python Data Types

### Part 1: **Create Variables with Different Data Types**
1. Define variables with the following data types: integer, float, boolean, and string.
2. Print each variable along with its type using the `type()` function.

#### Example:
```python
# Define variables
my_int = 10
my_float = 3.14
my_bool = True
my_string = "Hello, World!"

# Print variables and their types
print(my_int, type(my_int))
print(my_float, type(my_float))
print(my_bool, type(my_bool))
print(my_string, type(my_string))
```

---

### Part 2: **Perform Operations with Strings**
1. Concatenate two strings and print the result.
2. Multiply a string by an integer and print the repeated string.
3. Use the `len()` function to find the length of a string.

#### Example:
```python
# String operations
string1 = "Python"
string2 = " is fun!"
result = string1 + string2
print(result)  # Concatenation

repeated = string1 * 3
print(repeated)  # Repetition

length = len(result)
print("Length of the string:", length)
```

---

### Part 3: **Work with Booleans**
1. Create boolean variables using expressions (`5 > 3`, `10 == 15`, etc.).
2. Use the `not` operator to invert a boolean's value.
3. Print the results and their types.

#### Example:
```python
# Boolean expressions
bool1 = (5 > 3)
bool2 = (10 == 15)

print(bool1, type(bool1))  # True
print(bool2, type(bool2))  # False

# Invert boolean value
inverted = not bool1
print(inverted, type(inverted))  # False
```

---

### Part 4: **Explore Floats**
1. Create a float variable with a fractional value.
2. Use the `round()` function to round it to 2 decimal places.
3. Print the original and rounded values.

#### Example:
```python
# Float operations
pi = 22 / 7
rounded_pi = round(pi, 2)

print("Original:", pi)
print("Rounded:", rounded_pi)
```

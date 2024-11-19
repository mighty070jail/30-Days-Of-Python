Here is the entire content in markdown format:

# Introduction

Whenever you create a variable in Python, it has a value with a corresponding **data type**. There are many different data types, such as integers, floats, booleans, and strings, all of which we'll cover in this lesson. (This is just a small subset of the available data types -- there are also dictionaries, sets, lists, tuples, and much more.)

**Data types are important** because they determine what kinds of actions you can perform with them. For instance:

- You can divide two floats, but you cannot divide two strings.  
  Example:  
  `12.0 / 2.0` makes sense, but `"cat" / "dog"` does not.

To avoid errors, we need to make sure that the actions match the data types we are working with.

---

## Integers

Integers are **numbers without any fractional part** and can be:

- Positive (`1, 2, 3, ...`)
- Negative (`-1, -2, -3, ...`)
- Zero (`0`)

```python
x = 14
print(x)
print(type(x))

Output:

14
<class 'int'>

In the output above, <class 'int'> refers to the integer data type.


---

Floats

Floats are numbers with fractional parts. They can have many numbers after the decimal.

nearly_pi = 3.141592653589793
print(nearly_pi)
print(type(nearly_pi))

Output:

3.141592653589793
<class 'float'>

Specifying Floats with Fractions

almost_pi = 22 / 7
print(almost_pi)
print(type(almost_pi))

Output:

3.142857142857143
<class 'float'>

Using the round() Function

The round() function rounds a number to a specified number of decimal places.

rounded_pi = round(almost_pi, 5)
print(rounded_pi)
print(type(rounded_pi))

Output:

3.14286
<class 'float'>

Floats Without Fractional Parts

Whenever you write a number with a decimal point, Python recognizes it as a float, even if it has no fractional part.

y_float = 1.
print(y_float)
print(type(y_float))

Output:

1.0
<class 'float'>


---

Booleans

Booleans represent one of two values: True or False.

z_one = True
print(z_one)
print(type(z_one))

Output:

True
<class 'bool'>

z_two = False
print(z_two)
print(type(z_two))

Output:

False
<class 'bool'>

Booleans are often used to represent the truth value of an expression.

z_three = (1 < 2)
print(z_three)
print(type(z_three))

Output:

True
<class 'bool'>

We can invert a boolean value using the not keyword.

z_five = not z_four
print(z_five)
print(type(z_five))

Output:

True
<class 'bool'>


---

Strings

Strings are a collection of characters (letters, punctuation, numbers, or symbols) enclosed in quotation marks. They are commonly used to represent text.

w = "Hello, Python!"
print(w)
print(type(w))

Output:

Hello, Python!
<class 'str'>

Length of a String

You can find the length of a string using the len() function.

print(len(w))

Output:

14

Empty Strings

An empty string has a length of zero.

shortest_string = ""
print(type(shortest_string))
print(len(shortest_string))

Output:

<class 'str'>
0

Strings with Numbers

If a number is enclosed in quotation marks, it is treated as a string.

my_number = "1.12321"
print(my_number)
print(type(my_number))

Output:

1.12321
<class 'str'>

You can convert a string to a float if it's valid.

also_my_number = float(my_number)
print(also_my_number)
print(type(also_my_number))

Output:

1.12321
<class 'float'>


---

String Operations

You can add two strings to concatenate them:

new_string = "abc" + "def"
print(new_string)
print(type(new_string))

Output:

abcdef
<class 'str'>

You can also multiply a string by an integer to repeat it:

newest_string = "abc" * 3
print(newest_string)
print(type(newest_string))

Output:

abcabcabc
<class 'str'>

However, you cannot multiply a string by a float:

will_not_work = "abc" * 3.0

Error Output:

TypeError: can't multiply sequence by non-int of type 'float'

In the error message:

The "sequence" refers to the string "abc".

The "non-int of type 'float'" refers to the float 3.0.


Thus, the error can be rephrased as "can't multiply string by float."




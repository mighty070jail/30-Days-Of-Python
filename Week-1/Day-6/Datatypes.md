# Data Types in Python

## Introduction
Whenever you create a variable in Python, it has a value with a corresponding data type. Data types determine what kinds of actions can be performed. Some common data types include:  
- **Integers**  
- **Floats**  
- **Booleans**  
- **Strings**

This is just a subset; others include dictionaries, sets, lists, and tuples. For instance:
- You can divide two floats (`12.0 / 2.0`), but dividing strings (`"cat" / "dog"`) is not valid.

---

## Integers
Integers are numbers without fractional parts. They can be:
- Positive: `1, 2, 3, ...`
- Negative: `-1, -2, -3, ...`
- Zero: `0`

```python
x = 14
print(x)          # Prints: 14
print(type(x))    # Prints: <class 'int'>
```

---

## Floats
Floats are numbers with fractional parts. For example:

```python
nearly_pi = 3.141592653589793
print(nearly_pi)       # Prints: 3.141592653589793
print(type(nearly_pi)) # Prints: <class 'float'>
```

Fractions can also result in floats:

```python
almost_pi = 22 / 7
print(almost_pi)       # Prints: 3.142857142857143
print(type(almost_pi)) # Prints: <class 'float'>
```

### Rounding Floats
The `round()` function lets you round to a specified number of decimal places:

```python
rounded_pi = round(almost_pi, 5)
print(rounded_pi)      # Prints: 3.14286
print(type(rounded_pi)) # Prints: <class 'float'>
```

---

## Booleans
Booleans represent one of two values: **True** or **False**.

```python
z_one = True
print(z_one)          # Prints: True
print(type(z_one))    # Prints: <class 'bool'>

z_two = False
print(z_two)          # Prints: False
print(type(z_two))    # Prints: <class 'bool'>
```

Booleans are often used to represent the truth value of expressions:

```python
z_three = (1 < 2)
print(z_three)         # Prints: True
print(type(z_three))   # Prints: <class 'bool'>
```

The `not` operator switches the value of a boolean:

```python
z_five = not z_two
print(z_five)         # Prints: True
```

---

## Strings
Strings are collections of characters enclosed in quotation marks. They can include:
- Letters
- Digits
- Punctuation

```python
w = "Hello, Python!"
print(w)              # Prints: Hello, Python!
print(type(w))        # Prints: <class 'str'>
print(len(w))         # Prints: 14
```


### Converting Strings
You can convert strings to floats if they are numeric:

```python
my_number = "1.12321"
also_my_number = float(my_number)
print(also_my_number)        # Prints: 1.12321
print(type(also_my_number))  # Prints: <class 'float'>
```

### String Operations
You can concatenate strings with `+`:

```python
new_string = "abc" + "def"
print(new_string)  # Prints: abcdef
```

You can also multiply a string by an integer:

```python
repeated_string = "abc" * 3
print(repeated_string)  # Prints: abcabcabc
```

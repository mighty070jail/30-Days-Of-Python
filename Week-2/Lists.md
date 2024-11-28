# Lists

Lists in Python represent ordered sequences of values. Here is an example of how to create them:

```python
primes = [2, 3, 5, 7]
```

We can put other types of things in lists:

```python
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```

We can even make a list of lists:

```python
hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'],  # (Comma after the last element is optional)
]
```

Alternatively, written on one line for compactness:

```python
hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]
```

A list can contain a mix of different types of variables:

```python
my_favourite_things = [32, 'raindrops on roses', help]
# (Yes, Python's help function is *definitely* one of my favourite things)
```

## Indexing

You can access individual list elements with square brackets.

Which planet is closest to the sun? Python uses zero-based indexing, so the first element has index 0.

```python
planets[0]  # 'Mercury'
```

What's the next closest planet?

```python
planets[1]  # 'Venus'
```

Which planet is furthest from the sun?

```python
planets[-1]  # 'Neptune'
planets[-2]  # 'Uranus'
```

## Slicing

What are the first three planets? We can answer this question using slicing:

```python
planets[0:3]  # ['Mercury', 'Venus', 'Earth']
```

This expression starts from index 0 and continues up to but not including index 3. Both the start and end indices are optional:

```python
planets[:3]  # ['Mercury', 'Venus', 'Earth']
planets[3:]  # ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```

Negative indices can also be used:

```python
planets[1:-1]  # ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
planets[-3:]  # ['Saturn', 'Uranus', 'Neptune']
```

## Changing Lists

Lists are "mutable," meaning they can be modified in place. For example, to rename Mars:

```python
planets[3] = 'Malacandra'
```

To shorten the names of the first three planets:

```python
planets[:3] = ['Mur', 'Vee', 'Ur']
```

And to restore their original names:

```python
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars']
```

## List Functions

Some useful functions for lists:

- `len`: Get the length of a list.

```python
len(planets)  # 8
```

- `sorted`: Returns a sorted version of a list.

```python
sorted(planets)  # Alphabetical order
```

- `sum`: Returns the sum of a numeric list.

```python
primes = [2, 3, 5, 7]
sum(primes)  # 17
```

- `min` and `max`: Get the smallest or largest item.

```python
max(primes)  # 7
```

## Interlude: Objects

Everything in Python is an object. Objects carry attributes and methods accessible via dot syntax. For example:

```python
x = 12
print(x.imag)  # 0

c = 12 + 3j
print(c.imag)  # 3.0
```

Methods are functions attached to objects, e.g., `x.bit_length()`.

## List Methods

Common list methods:

- **`list.append`**: Adds an item to the end of a list.

```python
planets.append('Pluto')
```

- **`list.pop`**: Removes and returns the last element.

```python
planets.pop()  # 'Pluto'
```

- **`list.index`**: Returns the index of an element.

```python
planets.index('Earth')  # 2
```

Use the `in` operator to check for membership:

```python
'Earth' in planets  # True
'Calbefraques' in planets  # False
```

For a complete list of methods, call `help(planets)`.


**Your Turn**: Practice by writing your own code and experimenting with lists!

# Day-8: Introduction to Lists  

Say you want to organize the names of the flower species.

One way to do this is by organizing the names in a Python string.

```python
flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

print(type(flowers))
print(flowers)
```

Even better is to represent the same data in a Python list.  To create a list, you need to use square brackets (`[`, `]`) and separate each item with a comma.  Every item in the list is a Python string, so each is enclosed in quotation marks.

```python
flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)
```

At first glance, it doesn't look too different, whether you represent the information in a Python string or list.  But as you will see, there are a lot of tasks that you can more easily do with a list.  For instance, a list will make it easier to:
- get an item at a specified position (first, second, third, etc), 
- check the number of items, and
- add and remove items.

# Lists

## Length

We can count the number of entries in any list with `len()`, which is short for "length".  You need only supply the name of the list in the parentheses.

```python
# The list has ten entries
print(len(flowers_list))
```

## Indexing

We can refer to any item in the list according to its position in the list (first, second, third, etc).  This is called **indexing**.

Note that Python uses zero-based indexing, which means that:
- to pull the first entry in the list, you use 0,
- to pull the second entry in the list, you use 1, and
- to pull the final entry in the list, you use one less than the length of the list.

```python
print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])

# The list has length ten, so we refer to final entry with 9
print("Last entry:", flowers_list[9])
```

**Side Note**: You may have noticed that in the code cell above, we use a single `print()` to print multiple items (both a Python string (like `"First entry:"`) and a value from the list (like `flowers_list[0]`).  To print multiple things in Python with a single command, we need only separate them with a comma.

## Slicing

You can also pull a segment of a list (for instance, the first three entries or the last two entries).  This is called **slicing**.  For instance:
- to pull the first `x` entries, you use `[:x]`, and
- to pull the last `y` entries, you use `[-y:]`.

```python
print("First three entries:", flowers_list[:3])
print("Final two entries:", flowers_list[-2:])
```

As you can see above, when we slice a list, it returns a new, shortened list.


## Removing items

Remove an item from a list with `.remove()`, and put the item you would like to remove in parentheses.

```python
flowers_list.remove("globe thistle")
print(flowers_list)
```

## Adding items

Add an item to a list with `.append()`, and put the item you would like to add in parentheses.

```python
flowers_list.append("snapdragon")
print(flowers_list)
```

## Lists are not just for strings

So far, we have only worked with lists where each item in the list is a string.  But lists can have items with any data type, including booleans, integers, and floats.

As an example, consider hardcover book sales in the first week of April 2000 in a retail store.

```python
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
```

Here, `hardcover_sales` is a list of integers.  Similar to when working with strings, you can still do things like get the length, pull individual entries, and extend the list.

```python
print("Length of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])
```

You can also get the minimum with `min()` and the maximum with `max()`.

```python
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))
```

To add every item in the list, use `sum()`.

```python
print("Total books sold in one week:", sum(hardcover_sales))
```

We can also do similar calculations with slices of the list.  In the next code cell, we take the sum from the first five days (`sum(hardcover_sales[:5])`), and then divide by five to get the average number of books sold in the first five days.

```python
print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)
```

# Your turn
Read the following sections carefully and implement the code examples as part of your **30 Days of Python Challenge**.

---




*Have questions or comments? Visit the [course discussion forum](https://www.kaggle.com/learn/intro-to-programming/discussion) to chat with other learners.*

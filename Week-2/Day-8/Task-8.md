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

## Lists

### Length
We can count the number of entries in any list with `len()`, which is short for "length".  You need only supply the name of the list in the parentheses.

## Indexing
We can refer to any item in the list according to its position in the list (first, second, third, etc).  This is called **indexing**.

Note that Python uses zero-based indexing, which means that:
- to pull the first entry in the list, you use 0,
- to pull the second entry in the list, you use 1, and
- to pull the final entry in the list, you use one less than the length of the list.

We can use a single `print()` to print multiple items (both a Python string (like `"First entry:"`) and a value from the list (like `flowers_list[0]`).  To print multiple things in Python with a single command, we need only separate them with a comma.

## Slicing
You can also pull a segment of a list (for instance, the first three entries or the last two entries).  This is called **slicing**.  For instance:
- to pull the first `x` entries, you use `[:x]`, and
- to pull the last `y` entries, you use `[-y:]`.
When we slice a list, it returns a new, shortened list.

## Removing items
Remove an item from a list with `.remove()`, and put the item you would like to remove in parentheses.

## Adding items
Add an item to a list with `.append()`, and put the item you would like to add in parentheses.

# Your turn
Read the following sections and implement the code examples as part of your 30 Days of Python Challenge.
- Print the length of the list flowers_list
- Use indexing to print first, second and last entry of the list
- Use slicing to print the first three entries and final two entries of the list
- Remove "globe thistle" from the list
- Append "snapdragon" to the list

---

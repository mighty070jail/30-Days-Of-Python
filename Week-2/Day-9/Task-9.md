# Day-8: Introduction to Lists  

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

We can also do similar calculations with slices of the list. We can take the sum from the first five days (`sum(hardcover_sales[:5])`), and then divide by five to get the average number of books sold in the first five days.

```python
print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)
```

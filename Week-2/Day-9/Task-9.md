# Day-9: Lists of Integers

So far, we have only worked with lists where each item in the list is a string.  But lists can have items with any data type, including booleans, integers, and floats.

As an example, consider hardcover book sales in the first week of April 2000 in a retail store.

```python
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
```
Here, `hardcover_sales` is a list of integers.  

### Task: **List Operations**
- Similar to when working with strings, you can still do things like get the length, print individual entries, and extend the list.
- Also get the minimum with `min()` and the maximum with `max()`.
- Add every item in the list, use `sum()`.

We can also do similar calculations with slices of the list. We can take the sum from the first five days (`sum(hardcover_sales[:5])`), and then divide by five to get the average number of books sold in the first five days.

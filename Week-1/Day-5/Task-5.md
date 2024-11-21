# Day-5: Using Multiple Variables

It’s common for code to use multiple variables, especially when calculating complex problems with various inputs. Using variables improves code readability and makes it easier to verify and update calculations.

---

### **Task-1**: Calculate the Number of Seconds in 1 Year
#### **Task-2**: Compute the Number of Seconds in 4 Years

We need to calculate the total number of seconds using the following variables:

```python
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60
```
Write a Python script to perform the above calculations and verify the result: 1)31,536,000 seconds. 2)126,144,000 seconds

### Why Use Variables?

- **Readability:** Using variables like `num_years` and `days_per_year` makes it easier to follow the logic.
- **Error Reduction:** Variables allow for better tracking and debugging of each part of the calculation.
- **Flexibility:** Updating input values becomes simple. For example, accounting for leap years involves updating just one variable: `days_per_year`.

---

### Update to Include Leap Years

To improve accuracy, we can account for leap years by updating:

```python
days_per_year = 365.25
```

This slight change recalculates the total seconds while keeping the rest of the code intact.

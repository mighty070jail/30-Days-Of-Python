
# **Week 1: Python Fundamentals**


## **Day 1: Introduction to `print()`**
- **Task**:  
  Use the `print()` function to display a message.  
  - Print `"Hello, World!"` and an additional message of their choice (e.g., "Learning Python is exciting!").  

- **Goal**:  
  Get comfortable with `print()` for outputting text.

---

## **Day 2: Working with Variables**
- **Task**:  
  Create variables for their name, age, and favorite color.  
  - Use `print()` to display them in a sentence, e.g., `"My name is [name], I am [age] years old, and I love [color]."`

- **Goal**:  
  Understand variables and how to store and use data.

---

## **Day 3: Basic Arithmetic Operations**
- **Task**:  
  Define two numbers and display the result of adding, subtracting, multiplying, and dividing them.  
  - Example: Define `num1 = 10` and `num2 = 5`, then output their sum, difference, product, and quotient.

- **Goal**:  
  Learn basic arithmetic operators in Python.

---

## **Day 4: Python Exercises**

### **Exercise 1: Basic Variable Creation and Printing**
1. Create a variable `x` and assign it the value of 10.  
2. Create another variable `y` and assign it the value of 20.  
3. Print the values of `x` and `y`.  

---

### **Exercise 2: Swapping Variables**
1. Create two variables, `num1` and `num2`, and assign them values 5 and 10 respectively.  
2. Swap their values (so `num1` becomes 10 and `num2` becomes 5).  
3. Print the new values of `num1` and `num2`.  

---

### **Exercise 3: Combining Strings and Variables**
1. Create a variable `name` and assign it your name.  
2. Create another variable `greeting` and assign it the value `"Hello, "`.  
3. Combine `greeting` and `name` into a single message and print it.  

---

### **Exercise 4: Updating Variables**
1. Create a variable `counter` and set it to 0.  
2. Increment `counter` by 5 three times (using `+=`).  
3. Print the final value of `counter`.  

---

## **Day 5: Using Multiple Variables**

### **Task 1**: Calculate the Number of Seconds in 1 Year  
### **Task 2**: Compute the Number of Seconds in 4 Years  

We need to calculate the total number of seconds using the following variables:

```python
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60
```

---

## **Day 6: Explore and Practice Python Data Types**

### **Part 1: Create Variables with Different Data Types**
1. Define variables with the following data types: integer, float, boolean, and string.  
2. Print each variable along with its type using the `type()` function.  

---

### **Part 2: Perform Operations with Strings**
1. Concatenate two strings and print the result.  
2. Multiply a string by an integer and print the repeated string.  
3. Use the `len()` function to find the length of a string.  

---

### **Part 3: Work with Booleans**
1. Create boolean variables using expressions (`5 > 3`, `10 == 15`, etc.).  
2. Use the `not` operator to invert a boolean's value.  
3. Print the results and their types.  

---

### **Part 4: Explore Floats**
1. Create a float variable with a fractional value.  
2. Use the `round()` function to round it to 2 decimal places.  
3. Print the original and rounded values.  

---

## **Day 7: Python Applications**

### **Part 1: Calculating Compound Interest**
- **Task**:  
  Write a program to calculate the compound interest for a given principal amount, rate of interest, and time period.  

#### **Steps**:  
1. Accept three inputs from the user:  
   - Principal amount (`P`)  
   - Annual interest rate (`r`) in percentage  
   - Time period in years (`t`)  
2. Calculate the compound interest using the formula:  

   ```python
   A = P * (1 + r / (n * 100))**(n * t)
   compound_interest = A - P
   ```

3. Print the final amount (`A`) and the compound interest.  

#### **Example Output**:  
```
Enter the principal amount: 1000  
Enter the annual interest rate (%): 5  
Enter the time period (in years): 2  

The total amount after 2 years: 1102.5  
The compound interest earned: 102.5  
```

- **Goal**:  
  Understand how to use mathematical formulas and user inputs in Python programs.

---

### **Part 2: BMI (Body Mass Index) Calculator**
- **Task**:  
  Create a program to calculate BMI and categorize the user's health based on their BMI score.  

#### **Steps**:  
1. Accept two inputs from the user:  
   - Weight (in kilograms)  
   - Height (in meters)  
2. Calculate BMI using the formula:  

   ```python
   BMI = weight / (height ** 2)
   ```

3. Determine the BMI category based on the following ranges:  
   - BMI < 18.5: Underweight  
   - 18.5 ≤ BMI < 24.9: Normal weight  
   - 25 ≤ BMI < 29.9: Overweight  
   - BMI ≥ 30: Obese  

4. Print the calculated BMI and the category.  

#### **Example Output**:  
```
Enter your weight (kg): 70  
Enter your height (m): 1.75  

Your BMI is: 22.86  
You are classified as: Normal weight  
```

- **Goal**:  
  Apply mathematical operations and conditional statements in Python programs.

---

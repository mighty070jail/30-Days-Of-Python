# Day-7: Python Applications  

### Part-1: **Calculating Compound Interest**  
- **Task**: 
  Write a program to calculate the compound interest for a given principal amount, rate of interest, and time period.  

#### Steps:  
1. Accept three inputs from the user:  
   - Principal amount (`P`)  
   - Annual interest rate (`r`) in percentage  
   - Time period in years (`t`)  
2. Calculate the compound interest using the formula:
     A = P * (1 + r / (n * 100))**(n * t)
     compound_interest = A - P
4. Print the final amount (`A`) and the compound interest.  

#### Example Output:  
```
Enter the principal amount: 1000  
Enter the annual interest rate (%): 5  
Enter the time period (in years): 2  

The total amount after 2 years: 1102.5  
The compound interest earned: 102.5  
```  

- **Goal**: Understand how to use mathematical formulas and user inputs in Python programs.

---

### Part-2: **BMI (Body Mass Index) Calculator**  
- **Task**:  
  Create a program to calculate BMI and categorize the user's health based on their BMI score.  

#### Steps:  
1. Accept two inputs from the user:  
   - Weight (in kilograms)  
   - Height (in meters)  
2. Calculate BMI using the formula:  
     BMI = weight \height  
3. Determine the BMI category based on the following ranges:  
   - BMI < 18.5: Underweight  
   - 18.5 ≤ BMI < 24.9: Normal weight  
   - 25 ≤ BMI < 29.9: Overweight  
   - BMI ≥ 30: Obese  
4. Print the calculated BMI and the category.  

#### Example Output:  
```
Enter your weight (kg): 70  
Enter your height (m): 1.75  

Your BMI is: 22.86  
You are classified as: Normal weight  
```  

- **Goal**: Apply mathematical operations and conditional statements in Python programs.

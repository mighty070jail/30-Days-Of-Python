'''
Author:IRENE JIMMY
Date:23-11-24
'''

#PART1
# Descriptiom:Write a program to calculate the compound interest for a given principal amount, rate of interest, and time period.
principal_amt=int(input("Enter the principal amount:"))
annual_rate=int(input("Enter the annual interest rate (%):"))
tm_prd=int(input("Enter the time period(in years):"))
n=1
a = principal_amt * (1 + annual_rate / (n * 100)) ** (n * tm_prd)
compound_interest = a - principal_amt
print("The total amount after" ,tm_prd," years:",a)
print("The compound interest earned:",compound_interest)


#PART2
#Description:Create a program to calculate BMI and categorize the user's health based on their BMI score
num1=int(input("Enter your weight(in kilograms)"))
num2=float(input("Enter your height(in meters)"))
num3=num1/num2**2
print("Your BMI is",num3)
if(num3<18.5):
    print("You are classified as: Underweight")
elif(18.5<num3<24.9):
    print("You are classified as: Normal weight")
elif(25<num3<29.9):
    print("You are classified as: Overweight")
else:
    print("You are classified as: Obese")


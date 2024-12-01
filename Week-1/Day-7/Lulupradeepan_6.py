'''
Author:Lulu Pradeepan
Date:1-12-20204
Description:Python Applications
'''
#PART1:Calculating Compound interest

p=int(input("Enter the principal amount:"))
r=int(input("Enter the annual interest rate(%):"))
t=int(input("Enter the time period(in years):"))
n=1
A=p*(1+r/(n*100))**(n*t)
compound_interest=A-p
print("The total amount after 2 years:",A)
print("The compound interest earned:",compound_interest)

#PART2:BMI(Body Mass Index)Calculator

W=int(input("Enter your weight(kg):"))
H=float(input("Enter your height(m):"))
BMI=W/H
print("your BMI is",BMI)
if BMI<18.5:
    print("you are classified as Underweight")
elif 18.5<=BMI<24.9:
    print("You are classified as Normal Weight")
elif 25<=BMI<29.9:
    print("you are classified as Overweight")
else:
    print("you are classified as Obese")

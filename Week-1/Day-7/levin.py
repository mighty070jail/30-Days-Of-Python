"""
Author = Levin Abraham Jacob
Date = 25-11-2024
description = Write a program to calculate the compound interest for a given principal amount,
rate of interest, and time period.
"""
Principal_Amt = float(input("Enter the principal Amount = "))
Annual_Interest = float(input("Enter the Annual Interest = "))
Time_period = int(input("Enter the Time period = "))
n=1
A = Principal_Amt * (1 + Annual_Interest / (n * 100))**(n * Time_period)
Compound_Interest = A - Principal_Amt

print(f"Total Amount in {Time_period} Years is = {A}.")
print(f"Compound Interest = {Compound_Interest}. ")
#Create a program to calculate BMI and categorize the user's health based on their BMI score.
weight = float(input("Enter Your Current Weight = "))
Height = float(input("Enter Your Current Height = "))
BMI = weight /Height
if BMI<18.5 :
    print("Under Weight")
elif 18.5<= BMI <24.9 :
    print("Normal weight")
elif 25<=BMI < 29.9:
    print("Over Weight")
elif BMI>29.9:
    print("Obese")

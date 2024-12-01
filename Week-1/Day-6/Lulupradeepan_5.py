'''
Author:Lulu Pradeepan
Date:1-12-2024
Description:Python Data Types
'''
#PART1
#Define Variables
my_int=56
my_float=5.6
my_bool=True
my_string="Hello World"
#Print Variables and their types
print(my_int,type(my_int))
print(my_float,type(my_float))
print(my_bool,type(my_bool))
print(my_string,type(my_string))

#PART2
#String Operations
String_1="Python"
String_2=" is Fun"
result=String_1+String_2
print(result)
repeated=String_1*3
print(repeated)
length=len(result)
print("length of the string:",length)

#PART3
#Boolean expressions
bool_1=(6>3)
bool_2=10==2
print(bool_1,type(bool_1))
print(bool_2,type(bool_2))
#Invert boolean value
inverted=not bool_1
print(inverted,type(inverted))

#PART4
#Float Operations
pi=22/7
rounded_pi=round(pi,2)
print("original:",pi)
print("Rounded:",rounded_pi)
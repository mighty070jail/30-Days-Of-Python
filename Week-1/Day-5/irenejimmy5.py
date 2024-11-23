'''
Author:IRENE JIMMY
Date:21-11-24
Description:Task-1: Calculate the Number of Seconds in 1 Year
Task-2: Compute the Number of Seconds in 4 Years
'''

num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60
no_secs=secs_per_min*hours_per_day*days_per_year*mins_per_hour
print( "The Number of Seconds in 1 Year",no_secs)
no_sec4=no_secs*num_years
print("The Number of Seconds in 4 Years",no_sec4)
Using multiple variables¶
It's common for code to use multiple variables. This is especially useful when we have to do a long calculation with multiple inputs.

In the next code cell, we calculate the number of seconds in four years. This calculation uses five inputs.

# Create variables
num_years = 4
days_per_year = 365 
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)
126144000
As calculated above, there are 126144000 seconds in four years.

Note it is possible to do this calculation without variables as just 60 * 60 * 24 * 365 * 4, but it is much harder to check that the calculation without variables does not have some error, because it is not as readable. When we use variables (such as num_years, days_per_year, etc), we can better keep track of each part of the calculation and more easily check for and correct any mistakes.

Note that it is particularly useful to use variables when the values of the inputs can change. For instance, say we want to slightly improve our estimate by updating the value of the number of days in a year from 365 to 365.25, to account for leap years. Then we can change the value assigned to days_per_year without changing any of the other variables and redo the calculation.

# Update to include leap years
days_per_year = 365.25

# Calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)
126230400.0
Note: You might have noticed the .0 added at the end of the number, which might look unnecessary. This is caused by the fact that in the second calculation, we used a number with a fractional part (365.25), whereas the first calculation multipled just numbers with no fractional part. You'll learn more about this in Lesson 3, when we cover data types.
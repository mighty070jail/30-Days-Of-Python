#   Using multiple variables

It's common for code to use multiple variables. This is especially useful when calculating long problems with various inputs.

In this task, we calculate the number of seconds in four years. 
This calculation uses five variables:

                       num_years = 4
                       days_per_year = 365 
                       hours_per_day = 24
                       mins_per_hour = 60
                       secs_per_min = 60

**Task-1: Calculate the number of seconds in four years**

Check if the output is 126144000 seconds

---

**Note:** It is possible to do this calculation without variables as just 60 * 60 * 24 * 365 * 4, but it is much harder to check that the calculation without variables does not have some error because it is not as readable. When we use variables (such as num_years, days_per_year, etc), we can better keep track of each part of the calculation and more easily check for and correct any mistakes.


Note that it is particularly useful to use variables when the values of the inputs can change. For instance, say we want to slightly improve our estimate by updating the value of the number of days in a year from 365 to 365.25, to account for leap years. Then we can change the value assigned to days_per_year without changing any of the other variables and redo the calculation.

**Update to include leap years**
days_per_year = 365.25

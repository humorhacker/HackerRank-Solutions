'''
Objective:
In this challenge, you will work with arithmetic operators. 
Check out the Tutorial tab for learning materials and an instructional video.
https://www.hackerrank.com/challenges/30-operators/tutorial

Task:
Given the meal price (base cost of a meal), 
tip percent (the percentage of the meal price being added as tip), 
and tax percent (the percentage of the meal price being added as tax) for a meal, 
find and print the meal's total cost. Round the result to the nearest integer.

Example:
meal_cost = 100
tip_percent = 15
tax_percent = 8

A tip of 15% * 100 = 15, and the taxes are 8% * 100 = 8. 
Print the value 123 and return from the function.

Function Description
Complete the solve function in the editor below.
solve has the following parameters:
- int meal_cost: the cost of food before tip and tax
- int tip_percent: the tip percentage
- int tax_percent: the tax percentage

Returns The function returns nothing. 
Print the calculated value, rounded to the nearest integer.

Note: Be sure to use precise values for your calculations, 
or you may end up with an incorrectly rounded result.

Input Format:
There are 3 lines of numeric input:
The first line has a double, meal_cost (the cost of the meal before tax and tip).
The second line has an integer, tip_percent (the percentage of mealCost being added as tip).
The third line has an integer, tax_percent (the percentage of mealCost being added as tax).

Sample Input:
12.00
20
8

Sample Output:
15

Explanation:

Given:
meal_cost = 12, tip_percent = 20, tax_percent = 8

Calculations:
tip = 12 and 12/100 x 20 = 2.4
tax = 8 and 8/100 x 12 = 0.96
total_cost = meal_cost + tip + tax = 12 + 2.4 + 0.96 = 15.36
round(total_cost) = 15
We round to the nearest integer and print the result, 15.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)

'''

#Solution:
#!/bin/python3

import math #importing math module to use round function to round the result to the nearest integer 
import os #importing os module to use system function to read input from the user 
import random #importing random module to use random function 
import re #importing re module to use regular expression function 
import sys #importing sys module to use system function to read input from the user

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#
print('Welcome to the meal cost calculator!') 
# printing the welcome message (NOT NEEDED FOR THE SOLUTION, JUST FOR FUN!)
def solve(meal_cost, tip_percent, tax_percent): 
# defining function solve with 3 parameters meal_cost, tip_percent, tax_percent
    # Write your code here
    tip = meal_cost * tip_percent / 100 # calculating tip 
    tax = meal_cost * tax_percent / 100 # calculating tax
    total_cost = meal_cost + tip + tax # calculating total cost
    print(round(total_cost)) # printing the result by rounding the total cost to the nearest integer
    print(f'The total cost of the meal is: ${round(total_cost, 2)}') 
    # printing the result by rounding the total cost to the nearest 2 decimal places 
    #(NOT NEEDED FOR THE SOLUTION, JUST FOR FUN!)
    print('Thank you for using the meal cost calculator!') 
    # printing the thank you message (NOT NEEDED FOR THE SOLUTION, JUST FOR FUN!)

if __name__ == '__main__': #main function
    meal_cost = float(input('What is the price of the food? ').strip())  
    # taking input from the user and stripping the white spaces

    tip_percent = int(input('What is the percent of the tip? ').strip()) 
    # taking input from the user and stripping the white spaces

    tax_percent = int(input('What is the percent of the tax? ').strip()) 
    # taking input from the user and stripping the white spaces

    solve(meal_cost, tip_percent, tax_percent) 
    # calling the function solve with 3 parameters meal_cost, tip_percent, tax_percent
'''
Objective
Today, we are learning about an algorithmic concept called recursion. 
Check out the Tutorial tab for learning materials and an instructional video.
https://www.hackerrank.com/challenges/30-recursion/tutorial

Recursive Method for Calculating Factorial:

factorial(N) = N * factorial(N-1) otherwise N <= 1

Function Description:
Complete the factorial function in the editor below. 
Be sure to use recursion.

factorial has the following paramter:
    int n: an integer

Returns:
    int: the factorial of 'n'

Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, 
you will get a score of '0'.

Input Format:
A single integer, 'n' (the argument to pass to factorial).

Constraints:
    2 <= n <= 12
    Your submission must contain a recursive function named factorial.

Sample Input:
3

Sample Output:
6

Explanation:
Consider the following steps. 
After the recursive calls from step 1 to 3, 
results are accumulated from step 3 to 1.

    1. factorial(3) = 3 * factorial(2) = 3 * 2 = 6
    2. factorial(2) = 2 * factorial(1) = 2 * 1 = 2
    3. factorial(1) = 1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

'''

# Solution:
#!/bin/python3

import math # import the math module to use the math.factorial() function
import os # import the os module to interact with the operating system
import random # import the random module to generate random numbers
import re # import the re module (Regular Expression)
import sys # import the sys module to interact with the Python runtime environment

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n): # define the factorial function
    # Write your code here
    if n <= 1: # if n is less than or equal to 1
        return 1 # return 1
    else: # otherwise
        return n * factorial(n - 1) # return n times the factorial of n - 1

if __name__ == '__main__': # if the script is being run directly
    fptr = open(os.environ['OUTPUT_PATH'], 'w') # open the output file

    n = int(input().strip()) # input the integer n

    result = factorial(n) # call the factorial function

    fptr.write(str(result) + '\n') # write the result to the output file

    fptr.close() # close the output file

# Explanation:
'''
We import the math, os, random, re, and sys modules.
We define the factorial function.
If n is less than or equal to 1, we return 1.
Otherwise, we return n times the factorial of n - 1.
We input the integer n.
We call the factorial function.
We write the result to the output file. 
We close the output file.
'''
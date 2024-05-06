'''
Objective:
In this challenge, we will use loops to do some math. 
Check out the Tutorial tab to learn more.
https://www.hackerrank.com/challenges/30-loops/tutorial

Task:
Given an integer, n, print its first 10 multiples. 
Each multiple n x i (where 1 <= i <= 10) 
should be printed on a new line in the form: n x i = result.

Example: n = 3

The printout should look like this:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

Input Format:
A single integer, n.

Constraints:
    2 <= n <= 20

Output Format:
Print 10 lines of output; 
each line i (where 1 <= i <= 10) 
contains the result of n x i in the form:
n x i = result.

Sample Input:
2

Sample Output:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
'''
# Solution:
import math # This is the math module: This module provides access to the mathematical functions defined by the C standard.
import os # This is the os module: This module provides a way of using operating system dependent functionality.
import random # This is the random module: This module implements pseudo-random number generators for various distributions.
import re # This is the re module: This module provides regular expression matching operations similar to those found in Perl. 
import sys 
# The sys module: provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

if __name__ == '__main__': 
    # This is the main function: This is the entry point of the program
    n = int(input().strip()) 
    # Taking the input from the user and converting it to integer .strip() is used to remove the leading and trailing spaces
    for i in range(1, 11): 
        # This is the for loop: This loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
        result = n * i 
        # This is the result of the multiplication of n and i
        print(f"{n} x {i} = {result}") 
        # This is the print statement: This is used to print the result of the multiplication of n and i

# Explanation:
'''

The code provided is a solution to a problem that involves printing the first 10 multiples of a given integer `n`. 
Let's break down the code further:

1. The code imports several modules: `math`, `os`, `random`, `re`, and `sys`. These modules provide various functionalities related to mathematics, operating system operations, random number generation, regular expressions, and system-specific parameters and functions.

2. The `if __name__ == '__main__':` condition checks if the current module is being run as the main program. This allows the code inside this block to be executed only when the module is run directly, and not when it is imported as a module in another program.

3. The code prompts the user to enter an integer value for `n` using the `input()` function. The `int()` function is then used to convert the user input to an integer, and the `strip()` function is used to remove any leading or trailing spaces from the input.

4. The `for` loop is used to iterate over the range of numbers from 1 to 10 (inclusive). The `range()` function is a built-in function that generates a sequence of numbers. In this case, it generates the numbers 1, 2, 3, ..., 10.

5. Inside the loop, the variable `result` is calculated by multiplying `n` with the current value of `i`.

6. The `print()` function is used to display the result of the multiplication in the format `n x i = result`. The `f-string` syntax is used to format the string by embedding the values of `n`, `i`, and `result` into the string.

7. After the loop finishes executing, the program ends.

This code effectively prints the first 10 multiples of the given integer `n` in the desired format.

'''

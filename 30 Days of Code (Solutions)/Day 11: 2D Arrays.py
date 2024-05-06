'''
Objective:
Today, we are building on our knowledge of arrays by adding another dimension. 
Check out the Tutorial tab for learning materials and an instructional video.
https://www.hackerrank.com/challenges/30-2d-arrays/tutorial

Context:
Given a 6x6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values 
with indices falling in this pattern in A's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task:
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

Example:
In the array shown above, the maximum hourglass sum is 7 for the hourglass in the top left corner.

Input Format:
There are 6 lines of input, 
where each line contains 6 space-separated integers that describe the 2D Array A.

Constraints:
    -9 <= A[i][j] <= 9
    0 <= i,j <= 5

Output Format:
Print the maximum hourglass sum in A.

Sample Input:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output:
19

Explanation:

A contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0

The hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

'''

# Solution:
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__': # if the script is run directly

    arr = [] # initialize an empty list

    for _ in range(6): # iterate over a range of 6
        arr.append(list(map(int, input().rstrip().split()))) # append a list of integers to arr

    hourglass_sums = [] # initialize an empty list to store the sums of hourglasses
    for i in range(4): # iterate over a range of 4
        for j in range(4): # iterate over a range of 4
            hourglass_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2] 
            # calculate the sum of the hourglass
            hourglass_sums.append(hourglass_sum) # append the sum to hourglass_sums

    max_hourglass_sum = max(hourglass_sums) # find the maximum sum of the hourglasses
    print(max_hourglass_sum) # print the maximum sum of the hourglasses


# Explanation:
'''

The code you provided is a solution to a problem that involves printing 
the first 10 multiples of a given integer `n`. 
Let's break down the code further:

1. The code imports several modules: `math`, `os`, `random`, `re`, and `sys`. 
These modules provide various functionalities related to mathematics, operating system operations, 
random number generation, regular expressions, and system-specific parameters and functions.

2. The `if __name__ == '__main__':` 
condition checks if the current module is being run as the main program. 
This allows the code inside this block to be executed only when the module is run directly, 
and not when it is imported as a module in another program.

3. The code prompts the user to enter an integer value for `n` using the `input()` function. 
The `int()` function is then used to convert the user input to an integer, 
and the `strip()` function is used to remove any leading or trailing spaces from the input.

4. The `for` loop is used to iterate over the range of numbers from 1 to 10 (inclusive). 
The `range()` function is a built-in function that generates a sequence of numbers. 
In this case, it generates the numbers 1, 2, 3, ..., 10.

5. Inside the loop, the variable `result` is calculated by multiplying `n` 
with the current value of `i`.

6. The `print()` function is used to display the result of the multiplication
 in the format `n x i = result`. The `f-string` syntax is used to format the string 
 by embedding the values of `n`, `i`, and `result` into the string.

7. After the loop finishes executing, the program ends.

This code effectively prints the first 10 multiples of the given integer `n` in the desired format.
'''

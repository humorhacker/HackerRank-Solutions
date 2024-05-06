'''
Objective
In this challenge, we learn about conditional statements. 
Check out the Tutorial tab for learning materials and an instructional video.
https://www.hackerrank.com/challenges/30-conditional-statements/tutorial

Task
Given an integer, n, perform the following conditional actions:

- If n is odd, print Weird
- If n is even and in the inclusive range of 2 to 5, print: Not Weird
- If n is even and in the inclusive range of 6 to 20, print: Weird
- If n is even and greater than 20, print: Not Weird
Complete the stub code provided in your editor to print whether or not n is weird.

Input Format:
A single line containing a positive integer, n.

Constraints:
1 <= n <= 100

Output Format:
Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0:
3

Sample Output 0:
Weird

Sample Input 1:
24

Sample Output 1:
Not Weird

Explanation:
Sample Case 0: n = 3
n is odd and odd numbers are weird, so we print Weird.

Sample Case 1: n = 24
n > 20 and n is even, so it is not weird. Thus, we print Not Weird.

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())

'''

# Solution:

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__': # This is the main function
    N = int(input().strip()) # Taking the input from the user and converting it to integer 
#.strip() is used to remove the leading and trailing spaces
    if N % 2 != 0: # This is the case when the input is odd
        print("Weird")
    elif N % 2 == 0 and N in range(2, 6):
        print("Not Weird") # This is the case when the input is even and in the range of 2 to 5
    elif N % 2 == 0 and N in range(6, 21):
        print("Weird") # This is the case when the input is even and in the range of 6 to 20
    elif N % 2 == 0 and N > 20: 
        print("Not Weird") # This is the case when the input is even and greater than 20
    else:
        print("Weird") # This is the default case, if the input is not in the range of 1 to 100

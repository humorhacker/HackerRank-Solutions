'''
Objective:
Today, we will learn about the Array data structure. 
Check out the Tutorial tab for learning materials and an instructional video.
https://www.hackerrank.com/challenges/30-arrays/tutorial

Task:
Given an array, A, of N integers, 
print A's elements in reverse order as a single line of space-separated numbers.

Example:
A = [1, 2, 3, 4]

Print: '4 3 2 1'. Each integer is separated by one space.

Input Format:
The first line contains an integer, N (the size of our array).
The second line contains N space-separated integers that describe array A's elements.

Constraints:
    1 <= N <= 1000
    1 <= A[i] <= 10000, where A[i] is the ith integer in the array.

Output Format:
Print the elements of array A in reverse order as a single line of space-separated numbers.

Sample Input:
4
1 4 3 2

Sample Output:
2 3 4 1


#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

'''

# Solution:

#!/bin/python3

import math # This is a module that provides mathematical functions defined by the C standard.
import os # This module provides a way of using operating system dependent functionality.
import random # This module implements pseudo-random number generators for various distributions.
import re # This module provides regular expression matching operations similar to those found in Perl.
import sys # This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

if __name__ == '__main__': # This is the main function
    n = int(input().strip()) # This is the number of elements in the array
 # This is the array of integers that we will reverse and print as a single line of space-separated numbers
    arr = list(map(int, input().rstrip().split())) # .split() splits the string into a list of strings
    # .rstrip() removes any trailing whitespace from the right side of the string
# This prints the array in reverse order as a single line of space-separated numbers
print(' '.join(map(str, arr[::-1]))) # .join() joins the elements of the array into a single string
# The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
# The str() function returns a string representation of the object.
# The arr[::-1] reverses the array
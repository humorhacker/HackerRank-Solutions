'''Objective:
Today we will learn about running time, also known as time complexity. 
Check out the Tutorial tab for learning materials and an instructional video.
https://www.hackerrank.com/challenges/30-running-time-and-complexity/tutorial

Task:
A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
Given a number, n, determine and print whether it is Prime or Not prime.

Note: If possible, try to come up with a 0(square root of n) primality algorithm, 
or see what sort of optimizations you come up with for an 0(n) algorithm. 
Be sure to check out the Editorial after submitting your code.

Input Format

The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines contains an integer, T, to be tested for primality.

Constraints:
    1 <= T <= 30
    1 <= n <= 2 x 10^9

Output Format:
For each test case, print whether n is Prime or Not prime on a new line.

Sample Input:
3
12
5
7

Sample Output:
Not prime
Prime
Prime

Explanation:

Test Case 0: n = 12.
12 is divisible by numbers other than 1 and itself (i.e.: 2, 3, 4, 6), so we print Not prime on a new line.

Test Case 1: n = 5.
5 is only divisible 1 and itself, so we print Prime on a new line.

Test Case 2: n = 7.
7 is only divisible 1 and itself, so we print Prime on a new line. '''

# Solution:
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    if is_prime(n):
        print('Prime')
    else:
        print('Not prime')

# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)

# The code above is a simple implementation of the primality test.
# It is a simple implementation of the primality test.
# The is_prime function returns True if the number is prime and False otherwise.
# The function iterates from 3 to the square root of n, checking if n is divisible by any number in that range.
# If n is divisible by any number in that range, the function returns False.
# If the function completes the loop without finding a divisor, it returns True.
# The main code reads the number of test cases, t, and then reads t numbers.
# For each number, it calls the is_prime function and prints the result.
# The time complexity of this code is O(sqrt(n)), where n is the number being tested.
# The space complexity is O(1) because the code uses a constant amount of space regardless of the input size.
# This code is efficient for small inputs, but it may not be optimal for large inputs.
# For larger inputs, more advanced primality tests, such as the Miller-Rabin test, can be used to improve performance.
# The Miller-Rabin test is a probabilistic primality test that can determine if a number is prime with high probability.
# It is more complex than the simple implementation shown here but can be more efficient for larger numbers.
# The code above provides a basic primality test that works well for small inputs and demonstrates the concept of time complexity in algorithms.

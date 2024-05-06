'''
Objective
Today we will expand our knowledge of strings, 
combining it with what we have already learned about loops. 
Check out the Tutorial tab for learning materials and an instructional video.
https://www.hackerrank.com/challenges/30-review-loop/tutorial

Task
Given a string, S, of length N that is indexed from 0 to N - 1,
print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line 
(see the Sample below for more detail).

Note: 0 is considered to be an even index.

Example:
s = adbecf

Print: abc def

Input Format:
The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a string, S.

Constraints:
- 1 <= T <= 10
- 2 <= length of S <= 10000

Output Format:
For each String Sj (where 0 <= j <= T - 1), print Sj's even-indexed characters, 
followed by a space, followed by Sj's odd-indexed characters.

Sample Input:
2
Hacker
Rank

Sample Output:
Hce akr
Rn ak

Explanation:
Test Case 0: S = "Hacker"
S[0] = "H"
S[1] = "a"
S[2] = "c"
S[3] = "k"
S[4] = "e"
S[5] = "r"

The even indices are 0, 2, and 4, and the odd indices are 1, 3, and 5. 
We then print a single line of 2 space-separated strings; 
the first string contains the ordered characters from S's even indices (Hce), 
and the second string contains the ordered characters from S's odd indices (akr).

Test Case 1: S = "Rank"
S[0] = "R"
S[1] = "a"
S[2] = "n"
S[3] = "k"

The even indices are 0 and 2, and the odd indices are 1 and 3. 
We then print a single line of 2 space-separated strings; 
the first string contains the ordered characters from S's even indices (Rn), 
and the second string contains the ordered characters from S's odd indices (ak).

'''
# Solution:
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input()) # number of test cases
for i in range(T): # loop through the test cases
    S = input() # input the string
    print(S[::2], S[1::2]) # S[::2] is for even index and S[1::2] is for odd index

# Explanation:
'''
The code you provided is a solution to a problem that involves reading multiple test cases 
and printing the characters at even and odd indices of each input string.

Here's a step-by-step explanation of how the code works:

1. The first line of the code, `T = int(input())`, 
reads an integer from the standard input and assigns it to the variable `T`. 
This integer represents the number of test cases that will be provided.

2. The `for` loop `for i in range(T):` is used to iterate `T` times, 
which means it will execute the following code block for each test case.

3. Inside the loop, `S = input()` reads a string from the standard input 
and assigns it to the variable `S`. This string represents the input for the current test case.

4. The line `print(S[::2], S[1::2])` prints the characters at even and odd indices of the string `S`. 

   - `S[::2]` is a slicing operation that extracts the characters from `S` starting from index 0 
   and stepping by 2. This means it will include characters at even indices (0, 2, 4, etc.).
   
   - `S[1::2]` is a similar slicing operation, but it starts from index 1 and steps by 2. 
   This means it will include characters at odd indices (1, 3, 5, etc.).
   
   - The two sliced strings are separated by a space in the `print` statement, 
   so the output will display the characters at even indices followed by the characters at odd indices.

To summarize, this code reads the number of test cases, reads a string for each test case, 
and then prints the characters at even and odd indices of each input string.    

'''


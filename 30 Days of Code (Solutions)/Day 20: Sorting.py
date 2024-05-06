'''Objective:
Today, we're discussing a simple sorting algorithm called Bubble Sort. 
Check out the Tutorial tab for learning materials and an instructional video!
https://www.hackerrank.com/challenges/30-sorting/topics

Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }
    
    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}

Task:
Given an array, a, of size n distinct elements, 
sort the array in ascending order using the Bubble Sort algorithm above. 
Once sorted, print the following 3 lines:

1.Array is sorted in numSwaps swaps.
where numSwaps is the number of swaps that took place.
2.First Element: firstElement
where firstElement is the first element in the sorted array.
3.Last Element: lastElement
where lastElement is the last element in the sorted array.
Hint: To complete this challenge, 
you will need to add a variable that keeps a running tally of all swaps that occur during execution.

Example:
a = [4, 3, 1, 2]

original a: 4 3 1 2
round 1  a: 3 1 2 4 swaps this round: 3
round 2  a: 1 2 3 4 swaps this round: 2
round 3  a: 1 2 3 4 swaps this round: 0

In the first round, the  is swapped at each of the  comparisons, ending in the last position. 
In the second round, the  is swapped at  of the  comparisons. Finally, in the third round, 
no swaps are made so the iterations stop. The output is the following:

Array is sorted in 5 swaps.
First Element: 1
Last Element: 4

Input Format:
The first line contains an integer, n, the number of elements in array a.
The second line contains n space-separated integers that describe a[0], a[1],..., a[n-1].

Constraints:
    2 <= n <= 600
    1 <= a[i] <= 2 x 10^6, where 0 <= i < n.

Output Format:
Print the following three lines of output:
1.Array is sorted in numSwaps swaps.
where numSwaps is the number of swaps that took place.
2.First Element: firstElement
where  is the first element in the sorted array.
3.Last Element: lastElement
where lastElement is the last element in the sorted array.

Sample Input 0:
3
1 2 3

Sample Output 0:
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3

Explanation 0:
The array is already sorted, 
so 0 swaps take place and we print the necessary 3 lines of output shown above.

Sample Input 1:
3
3 2 1

Sample Output 1:
Array is sorted in 3 swaps.
First Element: 1
Last Element: 3

Explanation 1:
The array a = [3, 2, 1] is not sorted, so we perform the following 3 swaps. 
Each line shows a after each single element is swapped.

1. [3, 2, 1] -> [2, 3, 1]
2. [2, 3, 1] -> [2, 1, 3]
3. [2, 1, 3] -> [1, 2, 3]

After 3 swaps, the array is sorted.

# Provided by HackerRank:
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here

'''

# Solution:
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numSwaps = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                numSwaps += 1
    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

# Explanation:
# The code above is a simple implementation of the Bubble Sort algorithm.
# It iterates through the array and compares adjacent elements.
# If the elements are in decreasing order, it swaps them.
# The number of swaps is counted and printed at the end.
# The first and last elements of the sorted array are also printed.
# The time complexity of Bubble Sort is O(n^2) in the worst case.
# However, it is not the most efficient sorting algorithm for large datasets.
# It is mainly used for educational purposes and small datasets.
# For large datasets, more efficient algorithms like Quick Sort or Merge Sort are preferred.
# The code above demonstrates the Bubble Sort algorithm and prints the required output.
# The input is read from the user, and the output is printed as specified in the problem statement.
# The code is written in Python and can be executed in any Python environment.
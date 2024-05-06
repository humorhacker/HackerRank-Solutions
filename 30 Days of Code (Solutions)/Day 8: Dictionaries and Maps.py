'''
Objective:
Today, we're learning about Key-Value pair mappings using a Map or Dictionary data structure. 
Check out the Tutorial tab for learning materials and an instructional video!
https://www.hackerrank.com/challenges/30-dictionaries-and-maps/tutorial

Task:
Given 'n' names and phone numbers, assemble a phone book that maps friends' names 
to their respective phone numbers. 
You will then be given an unknown number of names to query your phone book for. 
For each 'name' queried, print the associated entry from your phone book on a new line 
in the form name=phoneNumber; if an entry for 'name' is not found, print 'Not found' instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format:
The first line contains an integer, 'n', denoting the number of entries in the phone book.
Each of the 'n' subsequent lines describes an entry in the form of 2 space-separated values 
on a single line. The first value is a friend's name, and the second value is an -digit phone number.

After the 'n' lines of phone book entries, there are an unknown number of lines of queries. 
Each line (query) contains a 'name' to look up, 
and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters and are first names only.

Constraints:
    1 <= n <= 10^5
    1 <= queries <= 10^5

Output Format:
On a new line for each query, print 'Not found' 
if the name has no corresponding entry in the phone book; 
otherwise, print the full 'name' and 'phoneNumber' in the format name=phoneNumber.

Sample Input:
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output:
sam=99912222
Not found
harry=12299933

Explanation:
We add the following 'n = 3' (Key,Value) pairs to our map so it looks like this:
'phoneBook = {(sam,99912222), (tom,11122222), (harry,12299933)}'
We then process each query and print key=value if the queried 'key' is found in the map; 
otherwise, we print 'Not found'.

Query 0: sam
Sam is one of the keys in our dictionary, so we print 'sam=99912222'.

Query 1: edward
Edward is not one of the keys in our dictionary, so we print 'Not found'.

Query 2: harry
Harry is one of the keys in our dictionary, so we print harry=12299933.

# Enter your code here. Read input from STDIN. Print output to STDOUT
*STDIN: Standard Input
*STDOUT: Standard Output
'''

# Solution:
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input()) # number of entries in the phone book
phoneBook = {} # phone book is a dictionary
for i in range(n):
    entry = input().split() # split the input into a list of strings
    phoneBook[entry[0]] = entry[1] # add the name and phone number to the phone book
while True:
    try:
        name = input() # input the name to look up
        if name in phoneBook: # if the name is in the phone book
            print(name + "=" + phoneBook[name]) # print the name and phone number
        else:
            print("Not found") # otherwise, print "Not found"
    except:
        break # break the loop if there is no more input

# Explanation:
'''
We first input the number of entries in the phone book.
We then create an empty dictionary called 'phoneBook'.
We then loop through the number of entries in the phone book.
We split the input into a list of strings.
We then add the name and phone number to the phone book.
We then loop through the queries.
We input the name to look up.
We then check if the name is in the phone book.
If the name is in the phone book, we print the name and phone number.
Otherwise, we print "Not found".
We then break the loop if there is no more input.
'''
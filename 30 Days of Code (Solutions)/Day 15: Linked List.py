'''
Objective:
Today we will work with a Linked List. 
Check out the Tutorial tab for learning materials and an instructional video.
https://www.hackerrank.com/challenges/30-linked-list/tutorial

A Node class is provided for you in the editor. A Node object has an integer data field, data, 
and a Node instance pointer, next, pointing to another node (i.e.: the next node in the list).

A Node insert function is also declared in your editor. It has two parameters: a pointer, head, 
pointing to the first node of a linked list, and an integer, data, 
that must be added to the end of the list as a new Node object.

Task:
Complete the insert function in your editor so that it creates a new Node 
(pass data as the Node constructor argument) and inserts it at the tail of the linked list 
referenced by the head parameter. Once the new node is added, return the reference to the head node.

Note: The head argument is null for an empty list.

Input Format:
The first line contains T, the number of elements to insert.
Each of the next T lines contains an integer to insert at the end of the list.

Output Format:
Return a reference to the head node of the linked list.

Sample Input:

STDIN   Function
-----   --------
4       T = 4
2       first data = 2
3
4
1       fourth data = 1

Sample Output:
2 3 4 1

Explanation:

T = 4, so your method will insert 4 nodes into an initially empty list.
First the code returns a new node that contains the data value 2 as the head of the list. 
Then create and insert nodes 3, 4, and 1 at the tail of the list.

Initial: head -> null

               Node n0
T0: head -> | data = 2 | null 

               Node n0           Node n1
T1: head -> | data = 2 | n1 -> | data = 3 | null

                Node n0           Node n1           Node n2
T2: head -> | data = 2 | n1 -> | data = 3 | n2 -> | data = 4 | null

                Node n0           Node n1           Node n2           Node n3
T3: head -> | data = 2 | n1 -> | data = 3 | n2 -> | data = 4 | n3 -> | data = 1 | null


# Provided by HackerRank:

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  

'''

# Solution:
class Node: 
    def __init__(self,data): # Constructor
        self.data = data # Data field
        self.next = None # Pointer to the next node
class Solution: 
    def display(self,head): # Display method
        current = head # Set current to head
        while current: # While current is not null
            print(current.data,end=' ') # Print the data of the current node
            current = current.next # Set current to the next node

    def insert(self,head,data): # Insert method
    #Complete this method
        if head == None: # If the list is empty
            head = Node(data) # Create a new node with the data
        else: # If the list is not empty
            current = head # Set current to head
            while current.next: # While the next node is not null
                current = current.next # Set current to the next node
            current.next = Node(data) # Create a new node with the data and set it as the next node
        return head # Return the head of the list
    
mylist= Solution() # Create an instance of the Solution class
T=int(input()) # Get the number of elements to insert
head=None # Set head to null
for i in range(T): # For each element to insert
    data=int(input()) # Get the data
    head=mylist.insert(head,data) # Insert the data into the list
mylist.display(head); # Display the list

# Explanation:
'''
The Node class is provided for you in the editor.
A Node object has an integer data field, data, and a Node instance pointer, next, pointing to another node
(i.e.: the next node in the list).
'''
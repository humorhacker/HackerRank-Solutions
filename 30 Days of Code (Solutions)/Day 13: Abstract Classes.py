'''
Objective:
Today, we will extend what we learned yesterday about Inheritance to Abstract Classes. 
Because this is a very specific object oriented concept, 
submissions are limited to the few languages that use this construct. 
Check out the Tutorial tab for learning materials and an instructional video.
https://www.hackerrank.com/challenges/30-abstract-classes/tutorial

Task
Given a Book class and a Solution class, write a MyBook class that does the following:
    Inherits from Book
    Has a parameterized constructor taking these  parameters:
    1. string 'title'
    2. string 'author'
    3. int 'price'
    Implements the Book class' abstract display() method so it prints these 3 lines:
    1. Title:, a space, and then the current instance's 'title'.
    2. Author:, a space, and then the current instance's 'author'.
    3. Price:, a space, and then the current instance's 'price'.

Note: Because these classes are being written in the same file, 
you must not use an access modifier (e.g.: ) when declaring MyBook or your code will not execute.

Input Format:
You are not responsible for reading any input from stdin. 
The Solution class creates a Book object and calls the MyBook class constructor 
(passing it the necessary arguments). It then calls the display method on the Book object.

Output Format:
The 'void display()' method should print and label the respective 'title', 'author', and  'price' 
of the MyBook object's instance (with each value on its own line) like so:

    Title: $title
    Author: $author
    Price: $price

Note: The $ is prepended to variable names to indicate they are placeholders for variables.

Sample Input:
The following input from stdin is handled by the locked stub code in your editor:
    The Alchemist
    Paulo Coelho
    248

Sample Output:
The following output is printed by your display() method:
    Title: The Alchemist
    Author: Paulo Coelho
    Price: 248

# Provided by HackerRank:
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()    

'''

# Solution:
from abc import ABCMeta, abstractmethod # Abstract Base Class (ABC) module is used to create abstract classes in Python.
class Book(object, metaclass=ABCMeta): # Book class is inherited from ABCMeta class.
    def __init__(self,title,author): # Constructor of Book class.
        self.title=title # Title of the book.
        self.author=author # Author of the book.
    @abstractmethod # This decorator is used to define a method as abstract method.
    def display(): pass # Abstract method to display the title, author and price of the book.

# Write MyBook class
class MyBook(Book): # MyBook class is inherited from Book class.
    def __init__(self, title, author, price): # Constructor of MyBook class.
        super().__init__(title, author) # Calling the constructor of Book class.
        self.price = price # Price of the book.
    def display(self): # Method to display the title, author and price of the book.
        print("Title:", self.title) # Display the title of the book.
        print("Author:", self.author) # Display the author of the book.
        print("Price:", self.price) # Display the price of the book.

title = input() # Input the title of the book.
author = input() # Input the author of the book.
price = int(input()) # Input the price of the book.
new_novel = MyBook(title, author, price) # Creating an object of MyBook class.
new_novel.display() # Display the title, author and price of the book.


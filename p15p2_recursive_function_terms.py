"""   
PROGRAM REQUEST p15p1
Consider the following series, defined recursively as follows:
f(n)= { 1               n=1
        f(n−1)+2**(n−1) n>1

(a) Write a recursive function that takes as its single argument an
integer ≥ 1 and prints out that number of terms from the above series.

(b) Write a program that prompts the user for a series of integers.
For each number entered the program should check that it is greater
than or equal to 1. If it is, it calls the function defined in part (a).
The program should stop when a zero or a negative number is entered.

(c) In your function, include some print statements that allow you to see
the operation of the recursion and its progress towards the base case.

PSEUDO CODE
def print_f(n):
    def f(n):
        Initialize f to 1
        if n == 1:
            return f
        else:
            # recusion
            # returns (f*(n-1)+2**(n-1))
            print("         ------Recursion f(n-1) happening below this line:-----")
            r = f*(n-1)
            s = 2**(n-1)
            print("         Calculated is recursion r=:", r, "; plus s=", s, "; returning:", r+s)
            return r + s
    for i in range(1,n+1):
         print(f(i))
terms = 1
while terms >=0:
    terms = int(input("Enter a number of terms you like to generate: "))
    print_f(terms)
"""
# function to print the terms
def print_f(n):
    # function for generating the terms
    def f(n):
        f=1
        if n == 1:
            return f
        else:
            # recusion
            # returns (f*(n-1)+2**(n-1))
            print("         ------Recursion f(n-1) happening below this line:-----")
            r = f*(n-1)
            s = 2**(n-1)
            print("         Calculated is recursion r=:", r, "; plus s=", s, "; returning:", r+s)
            return r + s
    for i in range(1,n+1):
        print(f(i))
n = 1
while n > 0:
    n = int(input("Enter a number of terms you like to generate: "))
    print_f(n)

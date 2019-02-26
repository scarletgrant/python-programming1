'''
NOTE!!!
The program asks for a function where the function itself prompts for the input.
Until a more elegant construction is found, don't forget to initialize n before calling the function

PROGRAM REQUEST p16p1
1. Consider the following series, defined recursively as follows:
f(n)={   2         n=1
         2×f(n−1)  n>1

(a) Write a recursive function that takes as its single argument an
integer ≥ 1 and prints out that number of terms from the above series.

(b) Write a program that prompts the user for a series of integers.
For each number entered the program should check that it is greater
than or equal to 1. If it is, it calls the function defined in part (a).
The program should stop when a zero or a negative number is entered.

(c) In your function, include some print statements that allow you to
see the operation of the recursion and its progress towards the base case.

PSEUDO CODE:
Define function f that takes single argument n to generate and print the terms
     go on while n >= 1 #Make sure to initialize n outside the function
        n = int(input("Enter a number of terms you like to generate: "))
        a = 2
        b = 0  
        print(a)
        if n == 1:
            pass
        else:
# including part c - see operation of recursion
            for i in range(2,n+1):
                c = 2 * (a-1)
                print("       calculation b: a-1=",a,"-1" )
                print("       returning b", a-1)
                print("       calculating c, 2*b, returning:",c)
                print(c)
                a = b
                b = c
# part b
n = 1
f(n)

'''
# part a
def f(n):
    while n >= 1:
        n = 1
        n = int(input("Enter a number of terms you like to generate: "))
        a = 2
        b = 0
        print(a)
        if n == 1:
            pass
        else:
# including part c - see operation of recursion
            for i in range(2,n+1):
                c = 2 * (a-1)
                print("       calculation b: a-1=",a,"-1" )
                print("       returning b", a-1)
                print("       calculating c, 2*b, returning:",c)
                print(c)
                a = b
                b = c
# part b
n = 1
f(n)


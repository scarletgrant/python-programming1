'''
PROGRAM
Write a program that prompts the user for a series of integers and,
for each of the numbers entered, uses a for loop to calculate that number
of terms of the Fibonacci Series.The program should stop when a negative number
is entered. 

PSEUDO-CODE
Set and initialize terms to 0
While terms >= 0:
# Prompt user for a the number (terms) to calculate that number of terms of the Ficonacci series.
    terms = int(input("Enter a number of terms you want to create the Fibonacci series for: "))
    Initialize index_a to 0, index_b to 1, index_fib to 1, i to 0
    For i in range (0, terms:
        index_fib = index_b + index_a
        print(index_b, " ", end = "")
        index_a = index_b, index_b = index_fib
    print() 
'''
terms = 0
while terms >= 0:
    terms = int(input("Enter a number of terms you want to create the Fibonacci series for: "))
    index_a, index_b, index_fib, i = 0, 1, 0, 0
    for i in range (0, terms):
        index_fib = index_b + index_a
        print(index_b, " ", end = "")
        index_a, index_b = index_b, index_fib
    print()

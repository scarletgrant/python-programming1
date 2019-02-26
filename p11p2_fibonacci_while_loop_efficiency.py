'''
PROGRAM
Write a program that prompts the user for an integer and uses a
while loop to calculate that number of terms of the Fibonacci Series.
Try to make the program as small and efficient as possible.

PSEUDO-CODE
# Prompt user for a number (terms)
terms = float(input("Enter a number of terms you want to create the Fibonacci series for: "))
Initialize counter to 1, index_a to 0, index_b to 1, index_fib to 1
While count <= terms:
    index_fib = index_b + index_a
    print(index_b, " ", end = "")
    increment counter with 1, index_a = index_b, index_b = index_fib
'''
terms = float(input("Enter a number of terms you want to create the Fibonacci series for: "))
count, index_a, index_b, index_fib = 1, 0, 1, 0
while count <= terms:
    index_fib = index_b + index_a
    print(index_b, " ", end = "")
    count, index_a, index_b = count +1, index_b, index_fib

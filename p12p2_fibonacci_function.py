'''
PROGRAM-REQUEST
(a) Write a function that takes as its argument a non-negative integer and
prints out that number of terms of the Fibonacci Series.
This function should not return an explicit value.
(b) Write a program that prompts the user for an integer and checks that
the number entered is non-negative.
If it is, it calls the function defined in part(a);
if not, it prints out an appropriate error message.

PSEUDO-CODE
# a. Function
Define function fibonacci: fib(x)
# x is the limit of terms
    Initialize index_a to 0, index_b to 1, index_fib to 0, i to 0
    For i in range (0, x):
        index_fib = index_b + index_a
        print(index_b, " ", end = "")
        index_a, index_b = index_b, index_fib
# b. Program
number= int(input('Enter a number (an int >= 0): '))
if number >= 0:
    print('The fibonacci terms are: ')
    fib(number)
else:
    print('Error: can only return fibonacci numbers with a non-negative number (>= 0')
'''
# a. Function
def fib(x):
    index_a, index_b, index_fib, i = 0, 1, 0, 0
    for i in range (0, x):
        index_fib = index_b + index_a
        print(index_b, " ", end = "")
        index_a, index_b = index_b, index_fib
# b. Program
number= int(input('Enter a number (an int >= 0): '))
if number >= 0:
    print('The fibonacci terms are: ')
    fib(number)
else:
    print('Error: can only calcualte the factorial of a non-negative number (>= 0')
    

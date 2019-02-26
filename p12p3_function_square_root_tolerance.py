'''
PROGRAM REQUEST
(a) Write a function that takes as its two arguments a number and a
tolerance and, using the technique exposed in lectures, returns an
approximation of the square root of the number that is within the tolerance.

(b) Write a program that prompts the user for a floating-point number and
checks that the number entered is non-negative. If it is, it calls the function
defined in part (a) with the number and a tolerance defined in the program and
prints out the square root of the number;
if not, it prints out an appropriate error message.

PSEUDO-CODE
# a. Function
Define function sqroot(number)
    Initialize epsilon, numGuesses, root = 1, 0, 0.0
    step = epsilon ** 2
    while abs(number - root ** 2) >= epsilon and root <= number:
        root += step
        numGuesses += 1
    if abs(number - root ** 2) < epsilon:
        return(root)
# b. Program
number = float(input('Enter the number for which you wish to calculate the square root: '))
epsilon = float(input('Enter the tolerance you like to use for calculating the square root: '))
if number >=0:
    print(sqroot(number))
else:
    print("Error. First number must be positive")
'''
# a. Function
def sqroot(number):
    epsilon, numGuesses, root = 1, 1, 0.0
    step = epsilon ** 2
    while abs(number - root ** 2) >= epsilon and root <= number:
        root += step
        numGuesses += 1
    if abs(number - root ** 2) < epsilon:
        return(root)
# b. Program
number = float(input('Enter the number for which you wish to calculate the square root: '))
epsilon = float(input('Enter the tolerance you like to use for calculating the square root: '))
if number >=0:
    print(sqroot(number))
else:
    print("Error. First number must be positive.")

'''
PROGRAM
Taking the program to calculate the factorial of a number presented in class,
investigate how it would be possible to have just two cases,
one where the number is less than 0 and one where it isn’t.
Rewrite the program to do this.

PSEUDO-CODE
# Prompt user for a number
number = int(input("Enter a number for which you wish to calculate the factorial (an int >= 0): "))
if number < 0:
    print("Error: Number entered was less then 0.")
else:
    set and initialize factorial to 1
    for i in range(1, number incremented with 1):
        factorial *= 1
    print("The factorial of", number, "is", factorial)
'''
number = int(input("Enter a positive (whole) number: "))
if number < 0:
    print("Number entered was less then 0.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("Factorial of", number, "is", factorial)

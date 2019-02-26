'''
INTRO
Write an algorithm in pseudocode first before writing a Python program.
Submit your algorithms in psuedocode as well as your Python programs.

PROGRAM
Write a program that prompts the user for a positive integer and uses
a for loop to calculate the factorial of that number.

PSEUDO-CODE
prompt user for a positive integer number
if number < 0:
    print("Number was negative")
else:
    if number == 0 or number == 1
        factorial = 1
    else:
        set and initialize factorial to 1
        for i in range(1, number incremented with 1):
            factorial *= 1
    print("The factorial of", number, "is", factorial)


'''
number = int(input("Enter a positive (whole) number: "))
if number < 0:
    print("Number was negative")
else:
    if number == 0 or number == 1:
        factorial = 1
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
    print("The factorial of", number, "is", factorial)

        

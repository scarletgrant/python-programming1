'''
PROGRAM
Write a program that uses a while loop to prompt the user for a series of
numbers, check whether each number is divisble by 2, 3, 5 or 7 and print
out which of 2, 3, 5 or 7 it is divisible by.

PSEUDO-CODE
Prompt user for a number 
While number is positive
        if number modulo 2 == 0
            print("2 ")
        if number modulo 3 == 0
            print(3 )
        if number modulo 5 == 0
            print(5 )
        if number modulo 7 == 0
            print(7 )
        Print a new line (with empty print statement print())
        Promt user for another number

'''
number = int(input("Please enter a (whole) number: "))
while number > 0:
    if number % 2 == 0:
        print("2 ", end = "")
    if number % 3 == 0:
        print("3 ", end = "")
    if number % 5 == 0:
        print("5 ", end = "")
    if number % 7 == 0:
        print("7 ", end = "")
# empty print statement to print a new line
    print()
    number = int(input("Please enter a number: "))

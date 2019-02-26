'''
PROGRAM
Write a program that prompts the user for a positive integer and uses a
while loop to calculate the sum of the integers up to and including that number.

PSEUDO-CODE
Set and initialize number to zero
Set and initialize total to zero
Prompt user for first positive integer
While number => 0:
    total += number
    print total
    Prompt user for a new positive integer

'''
number = 0
total = 0
number = int(input("Please enter a positive number: "))
while number >= 0:
    total += number
    print("Total is:", total)
    number = int(input("Please enter a positive number: "))

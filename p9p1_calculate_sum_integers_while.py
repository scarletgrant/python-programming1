'''
PROGRAM
Write a program that prompts the user for a positive integer and uses a
WHILE loop to calculate the sum of the integers up to and including that number.

PSEUDO-CODE
Prompt user for a positive integer called number
If number < 0:
    print("Number was negative")
    prompt user again for a positive integer called number
Else:
    Set and initialize sum_integers to zero, Set and initialize i to 1 (the first integer)
    While i <= number:
        sum_integers = sum_integers + i
        Increment i with 1
    print("The sum of integers up to and including", number, "is", sum_integers)    
'''    

number = int(input("Please enter a positive number: "))
if number < 0:
    print("Number was negative")
    number = int(input("Please enter a positive number: "))
else:
    sum_integers, i = 0, 1
    while i <= number:
        sum_integers += i
        i += 1
    print("The sum of integers up to and including", number, "is", sum_integers)

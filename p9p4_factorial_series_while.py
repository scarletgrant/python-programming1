'''
PROGRAM
Write a program that prompts the user for a series of positive integers and,
for each of the numbers entered, uses a while loop to calculate the factorial
of that number. The program should stop when a negative number is entered.

PSEUDO-CODE
prompt user for a positive integer number
while number >= 0:
    initialize factorial and count to zero
    while count <= number:
        factorial = factorial * count
        increment count
        print("The factorial of", number, "is", factorial)
    prompt user for another number = int(input("Enter a positive (whole) number: "))
'''
number = int(input("Enter a positive (whole) number: "))
while number >= 0:
    count, factorial = 1,1
    while count <= number:
        factorial *= count
        count += 1
    print("The factorial of", number, "is", factorial)
    number = int(input("Enter a positive (whole) number: "))

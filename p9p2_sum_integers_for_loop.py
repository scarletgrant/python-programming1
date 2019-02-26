'''
PROGRAM
Write a program that prompts the user for a series of positive integers and,
for each of the numbers entered, uses a FOR loop to calculate the sum of the
integers up to and including that number.
The program should stop when a non-positive number is entered.

PSEUDO-CODE
prompt user for a positive integer number
while number is positive
    initialize integer_sum to 0
    for number in range(1, number plus 1):
        integer_sum += number
    print("The sum of integers up to and including", number, "is", sum_integers)
    prompt user for another positive integer number
else:
    print("Number was negative")
'''
number = int(input("Enter a positive (whole) number: "))
while number >= 0:
    integer_sum = 0
    for number in range(1, number + 1):
        integer_sum += number
    print("The sum of integers up to and including", number, "is", integer_sum)
    number = int(input("Enter a positive (whole) number: "))
else:
    print("Number was negative")


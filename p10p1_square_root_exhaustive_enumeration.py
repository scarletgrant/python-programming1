'''
PROGRAM
Write a program that prompts the user for an integer and performs exhaustive
enumeration to find the integer square root of the number. By “exhaustive enumeration”,
we mean that we start at 0 and succcessively go through the integers, checking whether
the square of the integer is equal to the number entered.

If the number is not a perfect square, the program should print out a
message to that effect. The program should exit when a negative number
is entered.

PSEUDO-CODE
# Prompt user for a positive integer (number) to calculate the square root for
number = int(input("Please enter a (whole) number that you like to calculate the square root for: "))
If number >= 0
    Initialize square_root to zero
    While square_root ** 2 < number:
        square_root += 1
    if square_root ** 2 == number:
        print("Square root of", number, "is", square_root)
    else:
        print(number, "is not a perfect square.")     
'''
number = int(input("Please enter a (whole) number that you like to calculate the square root for: "))
if number >= 0:
    square_root = 0
    while square_root ** 2 < number:
        square_root += 1
    if square_root ** 2 == number:
        print("Square root of", number, "is", square_root)
    else:
        print(number, "is not a perfect square.")



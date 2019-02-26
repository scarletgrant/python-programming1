'''
PROGRAM 
Write a program that prompts the user for a series of integers and, for each of the numbers
entered, performs exhaustive enumeration to find the integer cube root of the number.
If the number is not a perfect cube, the program should print out a message to that effect.
Note that the program should work for negative numbers as well as positive numbers.
The program should exit when a 0 is entered.

PSEUDO-CODE
# Prompt user for a positive integer (number) to calculate the square root for
number = int(input("Please enter another (whole) number that you like to calculate the cube root for: "))
while number != 0
    Initialize cube_root to zero
    While cube_root ** 3 < abs(number):
        cube_root += 1
    if cube_root ** 3 == abs(number):
        if number < 0:
            cube_root = -cube_root
        print("Cube root of", number, "is", cube_root)
        number = int(input("Please enter another (whole) number that you like to calculate the cube root for: "))
    else:
        print(number, "is not a perfect cube.")     
'''
number = int(input("Please enter a (whole) number that you like to calculate the cube root for: "))
while number != 0:
    cube_root = 0
    while cube_root ** 3 < abs(number):
        cube_root += 1
    if cube_root ** 3 == abs(number):
        if number < 0:
            cube_root = -cube_root
        print("Cube root of", number, "is", cube_root)
        number = int(input("Please enter another (whole) number that you like to calculate the cube root for: "))
    else:
        print(number, "is not a perfect cube.")

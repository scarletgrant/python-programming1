'''
Implement the programs that illustrate the definition and use of functions
in Python from Monday’s lectures (Pages 4 and 5 of the notes).
Save these programs as p13p1.py and p13p2.py, respectively.

PSEUDO CODE
NOTE: This program does not take equal numbers into account.
Define function max to return the largest of two arguments a, b
    if a > b:
        return a
    else:
        return b
Prompt user for number1, a float
Prompt user for number2, a float
set variable 'biggest' as max(number1, number2)
print("The largest of", number1, "and", number2, "is", biggest)
print("Finished!")
'''

# Program to print out the largest of two numbers entered by the user
# Uses a function max
def max(a, b):
# Function that returns the largest of its two arguments
    if a > b:
        return a
    else:
        return b
# Prompt the user for two numbers
number1=float(input("Enter a number: "))
number2=float(input("Enter another number: "))
# Set a variable for max
biggest = max(number1, number2)
print("The largest of", number1, "and", number2, "is", biggest)
print("Finished!")

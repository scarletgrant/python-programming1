'''
Implement the program that uses the print_max function from Monday’s lectures
(Page 9 of the notes).
Ensure that you understand what is going on and how it works.
Save this program as p13p3.py.

PSEUDO CODE
NOTE: This program does not take equal numbers into account.
Define function that PRINTS out the largest of two arguments a, b
    Define max Function that RETURNS the largest of its two arguments a, b
        If a > b:
            Return a
        else:
            Return b      
    Prompt user for number1, a float
    Prompt user for number2, a float
    Print("The largest of", number1, "and", number2, "is", max(number1, number2))
    return
print_max()

'''

# Program to print out the largest of two numbers entered by the user
# Uses two functions: max and print_max
# Function that prints out the largest of two numbers

def print_max():
# Uses the function max to find the largest
    def max(a, b):
        # function that returns the largest of two arguments
        if a > b:
            return a
        else:
            return b
# Prompt the user for two numbers
    number1=float(input("Enter a number: "))
    number2=float(input("Enter another number: "))
    # print is included in the function here
    print("The largest of", number1, "and", number2, "is", max(number1, number2))
    return
print_max()
# print(print_max())
# (print_max)


'''
PROGRAM-REQUEST
a.Write a function that takes as its single argument a
non-negative integer and returns the factorial of the number.
b.Write a program that prompts the user for an integer and checks that the number
entered is non-negative. If it is, it calls the function defined in part (a)
and prints out the result; if not, it prints out an appropriate error message.

PSEUDO-CODE
# a. Function
Define function factorial
    Initialize result of factorial calcualtion to zero
    for i in range(1, x+1):
        result is result * i
    return result
# b. Program
prompt user for number
if number is bigger or equal to 0:
    print('The factorial of', number, 'is', fact(number))
else:
    print('Error: can only calcualte the factorial of a non-negative number (>= 0')
'''
import time
# a. Function
def fact(x):
    res = 1
    for i in range(1, x+1):
        res *= i
    return res
# b. Program
starttime=time.time()
number= int(input('Enter a number (an int >= 0): '))
if number >= 0:
    print('The factorial of', number, 'is', fact(number))
else:
    print('Error: can only calcualte the factorial of a non-negative number (>= 0')
endtime=time.time()
executiontime=endtime-starttime
print(executiontime)

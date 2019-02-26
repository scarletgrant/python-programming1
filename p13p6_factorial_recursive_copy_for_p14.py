"""
6.
(a)
Write a recursive function that takes as its single argument a non-negative
integer and returns the factorial of the number.

(b) Write a program that prompts the user for an integer and checks that the
number entered is non-negative. If it is, it calls the function defined in
part (a) and prints out the result;
if not, it prints out an appropriate error message.

(c) In your function, include some print statements that allow you to see the
operation of the recursion and its progress towards the base case.
Save this program as p13p6.py.

PSEUDO CODE
(a)
# Import time for practical 14
Define factorial(x):
    # (c)
    print("before recursion", x)
    if x equals zero:
        return 1
    else:
        calculation = x * factorial(x-1)
        # (c)
        print(calculation)
        return calculation
(b)
# Set timer: starttime=time.time()
Prompt user for an integer
if number >= 0:
    print(factorial(number))
else:
    print("Error. Number was negative.")
# End timer. endtime=time.time()
# Calculate execution time: executiontime=endtime-starttime
# print(executiontime)


"""
## base case is when you stop the recursion, as long as x is not zero
# (a)
import time
def factorial(x):
    print("before recursion", x)
    if x==0:
        return 1
    else:
        calculation =  x * factorial(x-1)
        print("Calculation so far: ", calculation)
        return calculation
# (b)
starttime=time.time()
number = int(input("Please enter a positive number: "))
if number >= 0:
    print("Factorial of ", number, "is: ", factorial(number))
else:
    print("Error. Number was negative.")
endtime=time.time()
executiontime=endtime-starttime
print(executiontime)

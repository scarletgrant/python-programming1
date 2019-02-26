
'''
PROGRAM REQUEST p16p2
Implement the program to calculate common divisors from Lecture 16.
You may use the solution on Pages 14–17 of the slides in your solution.
Save this program as p16p2.py.

PSEUDO CODE:
function findDivisors(num1, num2)
    initialize divisors
    for i from 1 to minimum(num1, num2) do
        if num1 mod i ==0 and num2 mod i == 0 then
            add i to divisors
    return divisors
Prompt user for 2 positive integers,
If the numbers entered are not positive then
    print out an error message
else
    find the common divisors
    print out the common divisors

'''
def findDivisors(num1, num2):
    """Finds comon divisors of num1 and num2 -
    Assumes that num1 and num2 are positive integers
    Returns a tuple containing the common divisors of num1 and num2"""
    divisors = ()
    for i in range (1, min(num1, num2) +1):
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i,)
    return(divisors)
            
num1 = int(input("Enter a positive integer: "))
num2 = int(input("Enter another positive integer: "))
if num1 <= 0 or num2 <= 0:
    print("numbers should be > 0.")
else:
#Get the common divisors and print them out
    divisors = findDivisors(num1, num2)
    print("The common divisors of", num1, "and", num2, "are:", divisors)



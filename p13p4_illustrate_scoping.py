"""
PROGRAM-REQUEST
Implement the program that illustrates scoping in Python
from Monday’s lectures (Page 12 of the notes).

PSEUDOCODE
# Program to illustrate scoping in Python
    
def f(x):
    # Function that adds 1 to its argument and prints it out
    print(’In function f:’)
    Increment x by 1
    Initialize y to 1
    print(’x is’, x)
    print(’y is’, y)
    print(’z is’, z)
    return x
Set x, y, z to resp. 5, 10, 15
print(’Before function f: ’)
print(’x is’, x)
print(’y is’, y)
print(’z is’, z)
z = f(x)
print(’After function f:’)
print(’x is’, x)
print(’y is’, y)
print(’z is’, z)
"""

def f(x):
    print("In function f: ")
    x += 1
    y=1
    print("x is", x)
    print("y is", y)
    print("z is", z)
    return x
x, y, z = 5, 10, 15
# above values are set before the function is called
print("Before function f:")
print("x is", x)
print("y is", y)
print("z is", z)
# function is called and variables xyz are printed as result of the function
z = f(x)
# values below are outside the function again, but - with the new value of z
# as result of the new value x of z
print("After function f:")
print("x is", x)
# y is the earlier initialized y since this is not
# changed outside the function like it is with z.
print("y is", y)
# z is the incremented x as calcualted in the function
print("z is", z)

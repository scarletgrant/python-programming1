"""
PROGRAM-REQUEST
Add some extra variables and operations on those variables in the program
from the previous question to ensure that you understand what is going on
and how it works.

EXPLANATION
# Program to illustrate scoping in Python
Before the function is called, the program takes the initializations as set after the function.
When the function is called it takes the numbers initialized inside the function.
§ = Changed or added values

PSEUDOCODE
# Program to illustrate scoping in Python
def f(x):
    # Function that adds 1 to its argument and prints it out
    print(’In function f:’)
    §Increment x by 10
    §Initialize y to 10
    §Increment b by 1
    §Initialize c to 11
    print(’x is’, x)
    print(’y is’, y)
    print(’z is’, z)
    return x
§ Set x, y, z, d, a, b, c to 5, 10, 15, 22, 40, 100, 130
print(’Before function f:’)
print(’x is’, x)
print(’y is’, y)
print(’z is’, z)
§ print("a is", a)
§ print("b is", b)
§ print("c is", c)
§ print("d is", d)
z = f(x)
print(’After function f:’)
print(’x is’, x)
print(’y is’, y)
print(’z is’, z)
§ print("a is", a)
§ print("b is", b)
§ print("c is", c)
§ print("d is", d)

"""

def f(x):
    print("In function f: ")
    x += 10
    y=10
    c = 11
    print("x is", x)
    print("y is", y)
    print("z is", z)
    print("a is", a)
    print("b is", b)
    print("c is", c)
    print("d is", d)
    return x
x, y, z, d, a, b, c = 5, 10, 15, 22, 40, 100, 130
# above values are set before the function is called
print("Before function f:")
print("x is", x)
print("y is", y)
print("z is", z)
print("a is", a)
print("b is", b)
print("c is", c)
print("d is", d)
# function is called and variables xyz is printed in the function
z = f(x)
# values below are outside the function again, but - with the new value of z
# as result of the earlier function
print("After function f:")
print("x is", x)
print("y is", y)
print("z is", z)
print("a is", a)
print("b is", b)
print("c is", c)
print("d is", d)

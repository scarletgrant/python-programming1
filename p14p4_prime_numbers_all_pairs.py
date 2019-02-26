"""
PROGRAM REQUEST 14.4
Using the program developed in Question 3 as a starting point,
or using a completely new technique if you prefer,
write a program that searches for prime numbers in a range of integers.
Again, the program should print out an appropriate message if a number
is a prime number. However, instead of printing out the first pair of
factors that it discovers for a non-prime number, this program should
print out all the pairs of factors.

PSEUDO CODE
# Program to illustrate the use of the else statement on a for loop
# Search for prime numbers in a range of integers
# We remove the break statement to keep it calculating for divisions

# Look for primr numbers in a range of integers
for number in range(1, 51):
    for i in range(2, number):
        if remainder of number / i == 0:
            print(number, 'equals', i, '*', number floor divisioned by i)
    else:
        # loop fell trhough without finding a factor
        print(number, 'is a prime number')
print("Finished!")

"""
for number in range(1, 51):
    for i in range(2, number):
        if number % i == 0:
            print(number, 'equals', i, '*', number//i)
    else:
        print(number, 'is a prime number')
print("Finished!")

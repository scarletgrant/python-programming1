"""
PROGRAM REQUEST 14.3
Implement the program that searches for prime numbers in a range of integers
and demonstrates the use of the else clause in a for loop in Python from
recent lectures (Lecture 13) (Page 16 of the notes).
Ensure that you understand how this program works.

PSEUDO CODE
# Program to illustrate the use of the else statement on a for loop
# Search for prime numbers in a range of integers
# This is the program exact from the lecture notes

# Look for prime numbers in a range of integers
for number in range(2, 20):
    for i in range(2, number):
        if remainder of number / i == 0:
            print(number, 'equals', i, '*', number floor divisioned by i)
            break
    else:
        # loop fell trhough without finding a factor
        print(number, 'is a prime number')
print("Finished!")

"""
for number in range(2, 20):
    for i in range(2, number):
        if number % i == 0:
            print(number, 'equals', i, '*', number//i)
            break
    else:
        print(number, 'is a prime number')
print("Finished!")

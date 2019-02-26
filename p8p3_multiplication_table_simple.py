'''
PROGRAM p8p3
Write a program that uses a while loop to generate a simple multiplication
table from 0 to 20. 

PSEUDO-CODE
initialize i to zero
prompt user for number j that set the table size
while i <= 20:
    print(i, " ", i*j)
    increment i+=1
    print a new line with print()

'''

i = 0
j = int(input("Please enter a number: "))
while i <= 20:
    print(i, " ", i*j)
    i+=1
    print()

             

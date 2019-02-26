'''
PROGRAM p10p3
Write a program that prompts the user for a series of strings and counts and prints
out the number of vowels (letters ’a’, ’e’, ’i’, ’o’ or ’u’) in each string.
The program should exit when an empty string is entered.

PSEUDO-CODE
Prompt user for a string
While string is not empty:
    Set and initialize amount of vowels to zero
    for i in string:
         if i equals vowals (lowercase and capital):
            increment vowals with one
    print("The amount of vowels in this string is:", vowals)
    Prompt user for another string
'''
string = input("Please enter a string: ")
while string != "":
    vowals = 0
    for i in string:
        if(i=="a" or i=="aA" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="u" or i=="U"):
            vowals += 1
    print("The amount of vowels in this string is:", vowals)
    string = input("Please enter a string: ")

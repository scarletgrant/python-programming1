'''
PROGRAM p8p4
Write a program that uses a while loop to prompt the user for a series
of integers and check whether each number is in one of the specified ranges:
• Number is equal to 0
• Number is greater than 0 and less than or equal to 20
• Number is greater than 20 and less than or equal to 40 • Number is greater
than 40 and less than or equal to 60
• Number is greater than 60 and less than or equal to 80
• Number is greater than 80 and less than or equal to 100
• Number is greater than 100
The program should also count the number of numbers in each range.
The program should continue until the user enters a number that is less than 0. Before finishing, the program should print out the analysis of the input, ie the number of numbers in each range.

PSEUDO-CODE
(NOTE: Program is not fully optimized yet for efficiency)
Set number and initialize to zero
Set range_0_20 and initialize to zero
Set range_20_40 and initialize to zero
Set range_40_60 and initialize to zero
Set range_60_80 and initialize to zero
Set range_80_100 and initialize to zero
Set range_100_plus and initialize to zero
While number >= zero
    prompt user for an integer
    print number
    if number is larger than zero (zero smaller than number) and number <=20:
        increment range_0_20 by 1
        print("number is in range 1-20")
    if number is in range(21,41):
        increment range_20_40 by 1
        print("number is in range 20-40")
    if number is in range(41,61):
        increment range_40_60 by 1
        print("number is in range 40-60")
    if number is in range(61,81):
        increment range_60_80  by 1
        print("number is in range 60-80")
    if number is in range(81,101):
        increment range_80_100 by 1
        print("number is in range 80-100")
    if number >= 100:
        increment range_100_plus by 1
        print("number is in range 100+")
    if number < 0:
        print("Entered numbers in range_0_20: ", range_0_20)
        print("Entered numbers in range_20_40: ", range_20_40)
        print("Entered numbers in range_40_60: ", range_40_60)
        print("Entered numbers in range_60_80: ", range_60_80)
        print("Entered numbers in range_80_100: ", range_80_100)
        print("Entered numbers in range_100+: ", range_100_plus)

'''
number = 0
range_0_20 = 0
range_20_40 = 0
range_40_60 = 0
range_60_80 = 0
range_80_100 = 0
range_100_plus = 0
while number >=0:
    number = int(input("Please enter a (whole) number: "))
    print(number)
    if 0 < number <= 20:
        range_0_20 +=1
        print("number is in range 1-20")
    if number in range(21,41):
        range_20_40 +=1
        print("number is in range 20-40")
    if number in range(41,61):
        range_40_60 +=1
        print("number is in range 40-60")
    if number in range(61,81):
        range_60_80 +=1
        print("number is in range 60-80")
    if number in range(81,101):
        range_80_100 +=1
        print("number is in range 80-100")
    if number >= 100:
        range_100_plus +=1
        print("number is in range 100+")
    if number < 0:
        print("Entered numbers in range_0_20: ", range_0_20)
        print("Entered numbers in range_20_40: ", range_20_40)
        print("Entered numbers in range_40_60: ", range_40_60)
        print("Entered numbers in range_60_80: ", range_60_80)
        print("Entered numbers in range_80_100: ", range_80_100)
        print("Entered numbers in range_100+: ", range_100_plus)
             

'''
PROGRAM-REQUEST
On any given day, a pizza company offers the choice of a certain number
of toppings for its pizzas. Depending on the day, it provides a fixed
number of toppings with its standard pizzas. Write a program that prompts
the user (the manager) for the number of possible toppings and the number
of toppings offered on the standard pizza and calculates the total number
of different combinations of toppings. Recall that the number of combinations
of k items from n possibilities is given by the formula nCk = n! / k!(n−k)!

NOTE by SG:
As per extra explenation of the request, this program only takes the combinations into
account when the maximum amount of toppings for the standdard pizza is used.
It also does expect to receive a higher number of possible toppings than number of toppings
on the standard pizza.
Here is a breakdown of the applied formula:
nCk = n! / k!(n−k)!
== number_possible_toppings! / number_toppings_standard! * 
        (number_possible_toppings - number_toppings_standard)!
== number_combinations = factorial_possible_toppings / (factorial_toppings_standard * 
        factorial_difference_toppings)

PSEUDO-CODE by SG:
Prompt manager for possible number of toppings for pizza's (n)
Prompt manager for fixed number of toppings on standard pizza's (k)
Set and initialize number of combinations to zero
Set and initialize factorial_possible_toppings to 1
Set and initialize factorial_toppings_standard to 1
difference_possible_standard_toppings = number_possible_toppings - number_toppings_standard
Set and initialize factorial_difference_toppings to 1
Check if entered numbers are larger than zero and if so then:
    for i in range(1, number_possible_toppings + 1):
        factorial_possible_toppings *= i
    for i in range(1, number_toppings_standard + 1):
        factorial_toppings_standard *= i
    for i in range(1, difference_possible_standard_toppings + 1):
        factorial_difference_toppings *= i        
    number_combinations = factorial_possible_toppings / (factorial_toppings_standard * 
        factorial_difference_toppings)
    print("Total number of combinations is", int(number_combinations))
Else:
    print("Total number of combinations is 0")
'''
number_possible_toppings = int(input("Enter the number of possible available toppings for the pizza's: "))
number_toppings_standard = int(input("Enter the number of toppings for the standard pizza's: "))
number_combinations = 0
factorial_possible_toppings, factorial_toppings_standard = 1, 1
difference_possible_standard_toppings = number_possible_toppings - number_toppings_standard
factorial_difference_toppings = 1
if number_possible_toppings >0 and number_toppings_standard > 0:
    for i in range(1, number_possible_toppings + 1):
        factorial_possible_toppings *= i
    for i in range(1, number_toppings_standard + 1):
        factorial_toppings_standard *= i
    for i in range(1, difference_possible_standard_toppings + 1):
        factorial_difference_toppings *= i        
    number_combinations = factorial_possible_toppings / (factorial_toppings_standard * 
        factorial_difference_toppings)
    print("Total number of combinations is", int(number_combinations))
else:
    print("Total number of combinations is 0")

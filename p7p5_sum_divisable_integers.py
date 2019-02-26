'''
PROGRAM
Write a program that sums the integers in the range 1–10000
that are divisble by 3 or by 5 and prints out the total.

PSEUDO-CODE
Set total_sum to zero
For i is in range 10001
    if i modulo 3 or 5 == 0:
        increment total_sum with i
if i = 10000
    print(total_sum)
'''
total_sum = 0
for i in range (10001):
    if (i % 3==0) or (i % 5==0):
        total_sum += i
if i ==10000:
    print(total_sum)


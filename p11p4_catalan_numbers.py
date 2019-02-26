'''
PROGRAM
The Catalan Numbers form a sequence of natural numbers.
They are defined as follows:
Cn = 1/n+1 [2n n] 
= (2n)!/(n+1)!n!
They can also be defined as follows:
C0 = 1 and Cn+1
= (2(2n+1)/n+2)Cn,n ≥ 0
The first few Catalan Numbers are:
C0 =1,C1 =1,C2 =2,C3 =5,C4 =14,C5 =42,C6 =132,C7 =429,C8 =1430.
Write a program that prompts the user for an integer and
calculates that number of Catalan Numbers.

NOTE BY SG
For simplicity, if the user enters zero, the user gets zero catalan numbers > the program ends 
The formula's needed for the code are:
C0 = 1
Cn+1 = Cn*((2*(2*n + 1))/(n+2))
n ≥ 0
The challanges here were:
-getting clearity in amount(amount) vs indexing and result(cn_) vs itteration of n(i)
-switching variables
-naming consistant variables

PSEUDO-CODE
Prompt user for # amount = int(input("Enter the amount of Catalan numbers you like to calculate: "))
Initialize n to zero
Set the initial catalan-result (cn_initial), seperately from n, and initialize it to 1, as C0 will be 1.
Set the next initial catalan-result (cn_new_initial) and initialize it to 1, as C1 will be 1 as well.
If amount > 0:
    print(cn_initial) #print the first number sperately
    amount = amount-1 # amount minus the already printed c
While n < amount and amount is bigger then 0 # while n < amount > 0:
# to clearly distinquish iteration from Numbers, the n in the formula is replaced by i here
    'Initialize' cn_next with the formula while in initial stage # c_next = cn_new_initial*((2*(2*i + 1))/(i+2))            
    Print(cn_next) & cast it to an integer # print(int(cn_next))
    Increment n with 1 # n+=1
    Make the (latest) 'next c' the 'new initial c' in the following loop #cn_new_initial=cn_next
    
'''
amount = int(input("Enter the amount of Catalan numbers you like to calculate: "))
i = 0
cn_initial = 1
cn_new_initial = 1
if amount > 0:
    print(cn_initial)
    amount = amount-1
while i < amount > 0:  
    cn_next = cn_new_initial*((2*(2*i + 1))/(i+2))
    print(int(cn_next))
    i+=1  
    cn_new_initial=cn_next

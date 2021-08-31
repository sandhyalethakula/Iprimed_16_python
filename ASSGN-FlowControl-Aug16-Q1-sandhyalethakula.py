"""
ACCEPT A NUMBER BETWEEN 5 AND 30 FROM THE USER. 
   a.IF THE NUMBER IS LESS THAN 10, MULTIPLY BY 5 AND PRINT THE RESULT
   b.IF THE NUMBER IS > 25, SUBTRACT 5 AND PRINT THE RESULT
   c.IF THE NUMBER IS >=10 AND <=15, ADD 5 AND PRINT THE RESULT
   d.IF THE NUMBER IS >20, DIVIDE BY 5 AND PRINT THE RESULT
   e.IF THE NUMBER DOES NOT SATISFY THESE CONDITIONS, PRINT THE NUMBER
"""

n=int(input('enter a number between 5 and 30: '))
if n>=5 and n<=30:
    if n<10:                #if n is less than 10 it multiplies by 5
        n=n*5
        print(n)
    elif n>25:              #if n is greater than 25 it substracts by5
        n=n-5
        print(n)
    elif n>=10 and n<=15:   #if n is between 10 and 15 it adds by 5
        n=n+5
        print(n)
    elif n>20:              #if n is greater than 20 it divides by 5
        n=n/5
        print(n)
else:
   print(n)

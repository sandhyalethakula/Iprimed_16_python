"""
ACCEPT A NUMBER BETWEEN 5 AND 30 FROM THE USER. 
   a.IF THE NUMBER IS LESS THAN 10, MULTIPLY BY 5 AND PRINT THE RESULT
   b.IF THE NUMBER IS > 25, SUBTRACT 5 AND PRINT THE RESULT
   c.IF THE NUMBER IS >=10 AND <=15, ADD 5 AND PRINT THE RESULT
   d.IF THE NUMBER IS >20, DIVIDE BY 5 AND PRINT THE RESULT
   e.IF THE NUMBER DOES NOT SATISFY THESE CONDITIONS, PRINT THE NUMBER
"""

n=int(input("Enter a number> "))    #ASKS USER TO ENTER A NUMBER
if n >= 5 and n<=30:                #CHECKS NUMBER IS BETWEEN 5 AND 30, IF NOT PRINTS ENTERED NUMBER
    if n < 10:                      #IF THE NUMBER IS LESS THAN 10, MULTIPLY BY 5 AND PRINT THE RESULT
        print(n*5)
    elif n> 25:                     #IF THE NUMBER IS > 25, SUBTRACT 5 AND PRINT THE RESULT
        print(n-5)
    elif n >=10 and n<=15:          #IF THE NUMBER IS >=10 AND <=15, ADD 5 AND PRINT THE RESULT
        print(n+5)
    elif n>20:                      #IF THE NUMBER IS >20, DIVIDE BY 5 AND PRINT THE RESULT
        print(n//5)
    else:                           #IF THE NUMBER DOES NOT SATISFY THESE CONDITIONS, PRINT THE NUMBER
        print(n)
else:
    print(n)                        #IF ALL ABOVE CONDITIONS FAILS IT PRINTS THE GIVEN NUMBER
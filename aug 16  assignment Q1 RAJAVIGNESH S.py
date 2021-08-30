"""ACCEPT A NUMBER BETWEEN 5 AND 30 FROM THE USER.

   a.IF THE NUMBER IS LESS THAN 10, MULTIPLY BY 5 AND PRINT THE RESULT

   b.IF THE NUMBER IS > 25, SUBTRACT 5 AND PRINT THE RESULT

   c.IF THE NUMBER IS >=10 AND <=15, ADD 5 AND PRINT THE RESULT

   d.IF THE NUMBER IS >20, DIVIDE BY 5 AND PRINT THE RESULT

   e.IF THE NUMBER DOES NOT SATISFY THESE CONDITIONS, PRINT THE NUMBER"""




n=int(input("enter a number between 5 and 30"))
if n<10:
    res=n*5
    print("Result",res)
elif n>25:
    res=n-5
    print("Result",res)
elif n>=10 and n<=15:
    res=n+5
    print("Result",res)
elif n>=20:
    res=n//5
    print("result",res)
else:
    print("Result",n)

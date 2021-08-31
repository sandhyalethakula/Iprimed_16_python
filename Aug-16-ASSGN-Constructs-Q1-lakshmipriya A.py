"""ACCEPT A NUMBER BETWEEN 5 AND 30 FROM THE USER.

   a.IF THE NUMBER IS LESS THAN 10, MULTIPLY BY 5 AND PRINT THE RESULT

   b.IF THE NUMBER IS > 25, SUBTRACT 5 AND PRINT THE RESULT

   c.IF THE NUMBER IS >=10 AND <=15, ADD 5 AND PRINT THE RESULT

   d.IF THE NUMBER IS >20, DIVIDE BY 5 AND PRINT THE RESULT

   e.IF THE NUMBER DOES NOT SATISFY THESE CONDITIONS, PRINT THE NUMBER"""


x=4
while x>=1:
    if x%4==0:
        print("party")
    elif x-2<0:
        print("cake")
    elif x/3==0:
        print("greetings")
    else:
        print("birthday")
    x=x-1

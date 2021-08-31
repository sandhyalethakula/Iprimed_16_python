"""ACCEPT A NUMBER BETWEEN 5 AND 30 FROM THE USER. 
   a.IF THE NUMBER IS LESS THAN 10, MULTIPLY BY 5 AND PRINT THE RESULT
   b.IF THE NUMBER IS > 25, SUBTRACT 5 AND PRINT THE RESULT
   c.IF THE NUMBER IS >=10 AND <=15, ADD 5 AND PRINT THE RESULT
   d.IF THE NUMBER IS >20, DIVIDE BY 5 AND PRINT THE RESULT
   e.IF THE NUMBER DOES NOT SATISFY THESE CONDITIONS, PRINT THE NUMBER
"""

while 1:
    num=input('enter  a number >')
    print("""
choose an option:
1=> add 10 to your number
2=>subtract 10 from your number
3=>multioly your number into 10
4=>divide your number by 10
0=>Quit""")
    choice=input('choice>')
    if choice=='1': print(int(num)+10)
    elif choice=='2': print(int(num)-10)
    elif choice=='3': print(int(num)*10)
    elif choice=='4': print(int(num)/10)
    elif choice=='0': break

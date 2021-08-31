"""

Write programs to generate the patterns

"""


num =int(input("Enter a number >"))         #asks user to enter a number
symbol = input("Enter a symbol >")          #asks user to choose a symbol which has to print in pattern

while num >0:
    print(symbol* num)                     #prints output pattern, length reduces by -1 for each loop 
    num-=1

num2 =int(input("Enter a number >"))

start =1
                                            #asks user to enter a number
while start <= num2:                        #print output from length 1 and ends at when start value equal to input value
    print(symbol * start)
    start+=1


num3 = int(input("Enter a number >"))       #asks user to enter a number
dup = num3

while num3 > 0:                             #prints output pattern, length reduces by -1 for each loop 
    print(symbol * dup)
    num3 -=1
    
num4 =int(input("Enter a number>"))         #asks user to enter a number
initial =2
while num4 >0:
    print(symbol* initial)
    initial +=2
    num4-=1

num5  = int(input("Enter a number>"))       #asks user to enter a number

while num5 > 0:
    print(symbol * num5)
    num5 -=3

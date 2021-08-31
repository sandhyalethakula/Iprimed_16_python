"""

Write programs to generate the patterns

"""


num =int(input("Enter a number >"))
symbol = input("Enter a symbol >")

while num >0:
    print(symbol* num)
    num-=1

num2 =int(input("Enter a number >"))

start =1

while start <= num2:
    print(symbol * start)
    start+=1


num3 = int(input("Enter a number >"))
initial=num3

while num3 > 0:
    print(symbol * initial)
    num3 -=1


num4  = int(input("Enter a number>"))
start=2
while num4 > 0:
	print(symbol * start)
	start+=2
	num4 -=1

num5=int(input("enter a number: "))
while num5>0:
	print(symbol*num5)
	num5-=3

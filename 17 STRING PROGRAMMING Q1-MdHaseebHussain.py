'''
1.People often forget closing parentheses when entering formulas. Write a program that asks the user to enter a 
formula and prints out whether the formula has the same number of opening and closing parentheses.
'''
f=input('enter the formula: ')
a=f.count('(')
b=f.count(')')
if a==b:
    print('your formula is correct')
else:
    print('opening or closing bracket is missing')


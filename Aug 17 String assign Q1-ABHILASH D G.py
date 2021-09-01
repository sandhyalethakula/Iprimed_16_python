''' people often forget closing parenthesis when entering formulas. write a program that asks the user to enter a formula and prints out whether the formula has the same number of opening and closing paranthesis.'''

parentheses_string = input('Enter string:\n')
count = 0
for char in parentheses_string:
    if char == "(":
        count += 1
    if char == ")":
        count -= 1
if count == 0:
    print('Parentheses balanced')
else:
    print('Parentheses unbalanced')

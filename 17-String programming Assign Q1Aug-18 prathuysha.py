''' people often forget closing parenthesis when entering formulas. write a program that asks the user to enter a formula and prints out whether the formula has the same number of opening and closing paranthesis.'''

formula=input("enter formula:")                #takes input from user
count1= formula.count(")")
count2=formula.count("(")
if count1==1 and count2>1:
	print("missing opening or closing parenthesis")
elif count2==1 and count1>1:
	print("missing opening or closing parenthesis")
else:
	print(formula)

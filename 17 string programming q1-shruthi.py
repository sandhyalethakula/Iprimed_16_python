'''To check if the formula has same number of parentheses :
Ask the user for the input for formula input '''

n=input("enter a formula: ")
a=n.count("(")
b=n.count(')')

if a == b :
    print ("There are same no of parentheses")
else:
    print("The parantheses are not equal.Please check again")
      



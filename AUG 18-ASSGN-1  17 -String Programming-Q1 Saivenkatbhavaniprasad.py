'''
People often forget closing parentheses when entering formulas. Write a program that asks the user to enter a 
formula and prints out whether the formula has the same number of opening and closing parentheses.
'''

formula = input("Enter formula >")                  #takes input from user
count1 = formula.count(")")                         #counts count of ) and ( in a formula
count2 = formula.count("(")
if count1 == count2:                                #if count of ) and ( are equal then it prints the output
    print("Correct formula")
else:
    print("Missing opening or closing parentheses") #if count doesn't match prints error with message
    

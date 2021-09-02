'''ACCEPT A NUMBER BETWEEN 5 AND 30 FROM THE USER. 
   a.IF THE NUMBER IS LESS THAN 10, MULTIPLY BY 5 AND PRINT THE RESULT
   b.IF THE NUMBER IS > 25, SUBTRACT 5 AND PRINT THE RESULT
   c.IF THE NUMBER IS >=10 AND <=15, ADD 5 AND PRINT THE RESULT
   d.IF THE NUMBER IS >20, DIVIDE BY 5 AND PRINT THE RESULT
   e.IF THE NUMBER DOES NOT SATISFY THESE CONDITIONS, PRINT THE NUMBER
'''
n1 = input("Enter an number between 5 and 30 :")
n = int(n1)
if n>5 and n<30: #IF THE NUMBER IS > 25, SUBTRACT 5 AND PRINT THE RESULT
	             #IF THE NUMBER IS >=10 AND <=15, ADD 5 AND PRINT THE RESULT
	             #IF THE NUMBER IS >20, DIVIDE BY 5 AND PRINT THE RESULT
	if n>25:
		print("The number is greater than 25 hence the result is ",n-5)
	elif n>=10 and n<=15:
		print("The number is between 10 and 15 hence the resut is ",n+5)
	elif n>20:
		print("The number is greater than 20 hence result is ",n/5)
	else:
		print(n," doesn't satisfy the conditions")

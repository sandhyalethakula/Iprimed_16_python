''' ACCEPT A NUMBER BETWEEN 5 AND 30 FROM THE USER. 
   a.IF THE NUMBER IS LESS THAN 10, MULTIPLY BY 5 AND PRINT THE RESULT
   b.IF THE NUMBER IS > 25, SUBTRACT 5 AND PRINT THE RESULT
   c.IF THE NUMBER IS >=10 AND <=15, ADD 5 AND PRINT THE RESULT
   d.IF THE NUMBER IS >20, DIVIDE BY 5 AND PRINT THE RESULT
   e.IF THE NUMBER DOES NOT SATISFY THESE CONDITIONS, PRINT THE NUMBER'''

n=int(input("enter a number:"))
if n>=5 and n<=30:
	if n<10:			#if the number is <10 multiply by 5 and print result
		print(n*5)
	elif n>25:			#if the number is >25 subtract 5 and print result
		print(n-5)
	elif n>=10 and n<=15:		#if the num is >=10 and <=15 add 5 and print result
		print(n+5)
	elif n>20:			#if the number
		print(n//5)
	else:
		print(n)
else:
	print(n)

'''ACCEPT 2 NUMBERS FROM THE USER. 
	IF THE 2 NUMBERS ARE EQUAL, PRINT THE APPROPRIATE MESSAGE
	IF THE FIRST NUMBER IS GREATER, PRINT THE APPROPRIATE MESSAGE
	IF THE SECOND NUMBER IS GREATER, PRINT THE APPROPRIATE MESSAGE
	IF THE USER DOES NOT ENTER A NUMBER, PRINT ERROR AND GET THE NUMBERS AGAIN''while True:'''


n1=input("enter 1st num:")#read the inputs from the user
n2=input("enter 2nd num:")
if n1.isdigit() and n2.isdigit(): #checking  for the inputs are digits
 if(n1>n2):     #if n1 is greater than n2
    print("n1 is greater")
    #break
 elif(n1==n2):    #if n1 is equal to n2
     print("equal")
     #break
 elif(n1<n2):     #if n1 is lesser than n2
     print("n2 is greater")
     #break
else:
    print("non number")# if inputs are not digits then print its not a number

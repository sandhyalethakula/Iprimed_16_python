"""1.      ACCEPT 2 NUMBERS FROM THE USER.

a.       IF THE 2 NUMBERS ARE EQUAL, PRINT THE APPROPRIATE MESSAGE

b.      IF THE FIRST NUMBER IS GREATER, PRINT THE APPROPRIATE MESSAGE

c.       IF THE SECOND NUMBER IS GREATER, PRINT THE APPROPRIATE MESSAGE

d.      IF THE USER DOES NOT ENTER A NUMBER, PRINT ERROR AND GET THE NUMBERS AGAIN"""



while True:
 n=input("enter 1st num:")
 n2=input("enter 2nd num:")
 if n.isdigit() and n2.isdigit():
    if(n>n2):
        print("n is greater")
        break
    elif(n==n2):
        print("equal")
        break
    elif(n<n2):
        print("n2 is greater")
        break
 else:
    print("non number")

 

            

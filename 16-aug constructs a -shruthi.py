"""1.accept two numbers from user
if two numbers are equal , print the message
if the first number is greater than the second print the message
if second number is greater than first , print the message
if the user does not enter a number , print error and get the number """


while 1:
    n=input('enter first number')
    m=input('enter second number')

    if n.isnumeric() and m.isnumeric():
        if n == m:
            print("Both are equal")
            break
        elif n > m:
            print("The first number is greater than second")
            break
        elif m >n :
            print("the second number is greater than first")
            break
    else:print("please enter a number")
        
        

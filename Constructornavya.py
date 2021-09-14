# ACCEPT 2 NUMBERS FROM THE USER. IF THE 2 NUMBERS ARE EQUAL, PRINT THE APPROPRIATE MESSAGE
#IF THE FIRST NUMBER IS GREATER, PRINT THE APPROPRIATE MESSAGE
#IF THE SECOND NUMBER IS GREATER, PRINT THE APPROPRIATE MESSAGE
#IF THE USER DOES NOT ENTER A NUMBER, PRINT ERROR AND GET THE NUMBERS AGAIN #


while 1:
    first_number = input("Enter first number > ")              #asks user to enter first and second number
    second_number = input('Enter second number > ')
    
    if first_number == '' and second_number == '':
        print('You missed to enter a number, Enter again!')     #if user doesn't enter any input, it will raise error,asks again to enter a number
    elif int(first_number) == int(second_number):
        print("Both numbers are equal")                         #if both numbers are equal prints both are equal and breaks loop
        break
    elif int(first_number) > int(second_number):
        print("First number is greater than Second number")     #if first number > second number prints first number is greater and breaks loop
        break
    elif int(second_number) > int(first_number):
        print("Second number is greater than First number")     #if second number > first number prints second number is greater and breaks loop
        break

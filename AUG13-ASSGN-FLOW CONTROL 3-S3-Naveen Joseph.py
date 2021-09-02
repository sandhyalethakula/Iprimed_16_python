'''Ask the user to enter userName
If the userName is wrong (not 'admin'), then ask the user to enter the user name again
If userName=='admin' then ask the user to enter password
If password is wrong, repeat the process
If password=='admin123' then greet the user and end the program'''
while 1:
    name = input("Enter the user name : ")#Entering the username
    if name == 'admin':
        password = input("Enter the password : ")#Entering the password
        if password == 'admin123':
            print("Welcome To The Window")
            break
        else:
            print("Wrong Password, Please try again")#Prints a message for wrong password
    else:
        print("Wrong Username, Please try again")#Prints a message for wrong username
        

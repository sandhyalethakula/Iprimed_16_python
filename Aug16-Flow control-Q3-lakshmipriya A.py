'''3.Ask the user to enter userName
If the userName is wrong (not 'admin'), then ask the user to enter the user name again
If userName=='admin' then ask the user to enter password
If password is wrong, repeat the process
If password=='admin123' then greet the user and end the program'''

while 1:
    username = input("Enter username >")        #checks username

    if username == "admin":                 #if correct ask password
        password = input("Enter password >")
        if password ==  "admin123":                 #if password is correct greet user and end
            print("Hello", username , "logged in successfully")
            break
        else:                                   #if wrong repeat again
            print(" Wrong password!")

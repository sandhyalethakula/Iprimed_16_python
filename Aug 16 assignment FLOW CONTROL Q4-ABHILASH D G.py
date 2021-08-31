"""2.Question
Ask the user to enter userName
If the userName is wrong (not 'admin'), then ask the user to enter the user name again
If userName=='admin' then ask the user to enter password
If password is wrong, repeat the process
If password=='admin123' then greet the user and end the program"""
#Program to enter username and password and checking if passswords is coorect
while True:
    name=input("enter user name")
    if name=="admin":
        paass=input("enter password")
        if paass=="admin123":
          print("hiii",name,paass)
          break





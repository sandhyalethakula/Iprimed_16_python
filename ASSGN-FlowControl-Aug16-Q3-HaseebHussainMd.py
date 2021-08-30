'''
1.ask the user to enter the username
2.if the username is admin then ask the user to enter the password.
3.if the password is admin123 then greet the user and end the program.
4.if the password is not admin123 then display wrong password.
3.if the username is not admin then ask the user to enter the username again.'''




while True:
    UserName=input('enter the user name : ')
    if UserName=='admin':
        password=input('enter the passsword : ')
        if password =='admin123':
            print('hello',UserName)
            break
        else:
           print('wrong password')
        

    

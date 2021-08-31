'''
1.ask the user to enter the username
2.if the username is admin then ask the user to enter the password.
3.if the password is admin123 then greet the user and end the program.
4.if the password is not admin123 then display wrong password.
3.if the username is not admin then ask the user to enter the username again.'''




while True:
    UserName=input('enter the user name : ')     #asks user to enter name
    if UserName=='Jyoti':
        password=input('enter the passsword : ')  #asks user to enter pwd  
        if password =='jan369':                    #checks pwd 
            print('hello',UserName)
            break
        else:
           print('wrong password')

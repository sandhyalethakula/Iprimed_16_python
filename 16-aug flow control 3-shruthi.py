"""Requirement:
1.ask the user to enter username
2. if the username is wrong , then ask them enter username again
3.if the username== admin, then ask to enter password
4. if password is wrong repeat the process
5.if password=="admin123" , greet the user """


while 1:
    n=input("enter your username:")
    if n =="admin":
        p=input("enter your password:")
        if p =="admin123":
            print("welcome",n)
            break
        else:
            print("enter correct password")
    else:
        print("enter correct username")
            

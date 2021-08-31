""" Ask the user to enter username
       if the user name is wrong then ask user to enter the username again
            if user is correct then ask the user to enter the password
                 if password is wrong repeat the process
                      if both are correct then greet the user"""





while True:
    name=input("enter user name")
    if name=="admin":
        paass=input("enter password")
        if paass=="admin123":
          print("HELLO",name,paass)
          break
    
    

student_details=[]                      #empty list to add student course details
choose_a_number =''
while 1:
    if choose_a_number == '':
        choose_a_number = input("Choose 0 to Quit, 1 to Accept & store your course data, 2 to Read the entered data > ")            #Ask user input to perform specific task in list mentioned
    elif choose_a_number == "0":
        break
    elif choose_a_number == "1":
        name = input("Enter your name >")                                               #Ask for user's name
        course = input("Chose courses:- python =>15000,java =.8000,rust=>10000,ruby =>20000 >")                       #Ask for course
        payment = input("Choose payment mode card:-1, e-wallet:-2 >")                   #Ask payment mode
        if course == "python":                                                          #checks the course name and procede to fee
            if payment == "1":
                fee = 15000+500
            else:
                fee = 15000 - (15000*5/100)                                             #if payment mode is card additional 500 charge apply or choose e-wallet to get 5% discount
        elif course == "java":
            if payment == "1":
                fee = 8000+500
            else:
                fee = 8000 - (8000*5/100)
        elif course == "ruby":
            if payment == "1":
                fee = 10000+500
            else:
                fee = 10000 - (10000*5/100)
        elif course == "rust":
            if payment == "1":
                fee = 20000+500
            else:
                fee = 20000 - (20000*5/100)
        if course != "" and fee > 0 and name!= '':
            student_details.append(("Name:- {}".format(name),"Course:- {}".format(course),"Fee:- {}".format(fee)))          #if users enters correct details a new list is created and append to empty list
        else:
            print("You missed to fill course or payment mode or name check again and Fill the Details!")             #if user does'nt enter any details or missed any it asks again
    elif choose_a_number == "2":
        for i in student_details:                                               #iterate each value in student_details, convert the details into list and print with comma separated
            details = list(i)
            print(", ".join(details))
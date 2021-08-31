'''
Code based assessment
````
1.Question
A student has joined a course costing as per the given table. 
If the fee is paid via card, an additional service charge of Rs. 500/- is added but if payment is made through e-wallet, a discount of 5% is given for the payment. 

Use this reference table:
python	15000
java   	8000            
ruby   	10000         
rust   	20000          

Write a program to: 
PROMPT ASKING THE USER TO CHOOSE:
    0 TO QUIT
    1 TO ACCEPT & STORE STUDENT DATA - (CREATE) - Collect multiple
    2 VIEW ALL THE ENTERED DATA - (READ)
    


DO AS PER THE USER'S CHOICE.
1. Collect Name, Course, modeOfPayment / store in tuple when finished 
2. display all entered data neatly
'''

student_details=[]                      #empty list to add student course details
choose_a_number=''
ans="y"
while 1:
    if choose_a_number =='':                                #checking the choose_a_number or ans to ask the to enter input as 0 or 1 or 2
        print("#"* 10, "STUDENT MANAGEMENT MENU","#"*10)
        print('''Choose:
0 to Quit the app,
1 to Create data,
2 to Display data ''')
        choose_a_number = input("Enter > ")            #Ask user input to perform specific task in list mentioned
        ans="y"                                                             #changing ans to y to avoid process errors
    elif choose_a_number == "0":
        print("Quit selected")
        print()
        num=0
        if len(student_details) == 0:
            print("Course enrollement is quit..")
            print("---Empty no info---")
        else:
            print("Course enrollement is quit..")
            print("Student who enrolled courses")
            for i in student_details:                                               #iterate each value in student_details, convert the details into list and print with comma separated
                details = list(i)
                num+=1
                print("        ",str(num)+".",", ".join(details))
                print()
        choose_a_number = ''  
        break
    elif choose_a_number == "1" and ans == "y":                                         #if choose_a_number is 1 and ans is y then it asks user to enroll course     
        if len(student_details) == 0:
            print("~"*20)
            print("        Create selected")
            print('''Fees:
    Python - 15000,
    Java - 8000,
    Ruby - 10000,
    Rust - 20000

    payment mode:
    1.Card - 500RS/- Extra charge,
    2.E-Wallet - 5% Discount''')
        name = input("        Enter name >")                                                                        #Ask for user's name
        course = input("        Enter a course >")                                              #Ask for course number
        payment = input("        Enter paymode number >")                                               #Ask payment mode
        if course == "python":                                                              #checks the course name and procede to fee
            if payment == "1":
                fee = 15000+500
            else:
                fee = 15000 - (15000*5/100)                                              #if payment mode is card additional 500 charge apply or choose e-wallet to get 5% discount
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
        if course in "pythonjavarustruby" and payment != '' and name!= '':                         #if users enters correct details a new tuple is created and append to studet_details list
            student_details.append(("Name:- {}".format(name),"Course:- {}".format(course),"Fee:- {}".format(fee)))         
            ans = input("        Enter y to continue or n to quit > ")                                  #After succesful creation of details ask user to continue or quit enrollment
        else:
            print("You missed to fill course or payment mode or name check again and Fill the Details!")             #if user does'nt enter any details or missed any it asks again
    elif ans == "n":
        choose_a_number = ''
    elif choose_a_number == "2":
        print("~"*20)
        print("        DISPLAY selected - Student who enrolled courses")
        print()
        num=0
        if len(student_details) ==0:
            print("---Empty no info---")
        else:
            for i in student_details:                                               #iterate each value in student_details, convert the details into list and print with comma separated
                details = list(i)
                num+=1
                print("        ",str(num)+".",", ".join(details))
                print()
        choose_a_number = ''                                        #changes choose_a_number to empty to end infinite loop
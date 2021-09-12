'''
Code based assessment
``````````````````````
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
    3 TO DELETE DATA
    4 TO EDIT THE STORED DATA
    5 TO FILTER THE STORED DATA
    
DO AS PER THE USER'S CHOICE.
1. Collect Name, Course, modeOfPayment / store in tuple when finished 
2. display all entered data neatly
3. delete the data of user entered id
4. edit the data
5. filter the data
'''
courses = ["Python","Java", "Ruby","Rust"]                  #courses list
student_details=[]                                          #empty list to add student course details
choose_a_number=''
pym=["Card","E-wallet"]                                     #payment options list
ans="y"                                                     #default ans yes
while 1:
    if choose_a_number =='':                                #checking the choose_a_number or ans to ask the to enter input as 0 or 1 or 2
        print("-"*60)
        print("#"* 10, "STUDENT MANAGEMENT MENU","#"*10)
        print("-"*60)
        print()
        choose_a_number = input('''Choose:
0 to Quit the app,
1 to Create data,
2 to Display data,
3 to Delete your data,
4 to Edit your data,
5 to Filter the data
Enter > ''')                                                            #Ask user input to perform specific task in list mentioned
        ans="y"                                                         #changing ans to y to avoid process errors
    elif choose_a_number == "0":
        print("~"*20)
        print("        Quit selected")
        print()
        num=0
        if len(student_details) == 0:
            print("Course enrollement is quit..")
            print("---Empty no info---")
        else:
            print("        Course enrollement is quit..")
            print("        Student who enrolled courses")
            print()
            for i in student_details:                                   #iterate each value in student_details, convert the details into list and print with comma separated
                details = list(i)
                num+=1
                print("        ",str(num)+".", " ".join(details))
                print()
        choose_a_number = ''  
        break
    elif choose_a_number == "1" and ans == "y":                         #if choose_a_number is 1 and ans is y then it asks user to enroll course     
        if len(student_details) == 0 or name !='':
            print("~"*20)
            print("        Create selected")
            print()
        name = input("        Enter name >")                            #Ask for user's name
        course = input('''
 Courses & Fees:
        1 to select Python - 15000,
        2 to select Java - 8000,
        3 to select Ruby - 10000,
        4 to select Rust - 20000
            
        Enter a course >''')                                            #Ask for course number
        payment = input('''
 payment mode:
        1.Card - 500RS/- Extra charge,
        2.E-Wallet - 5% Discount
        Enter paymode number > ''')                                     #Ask payment mode
        if course == "1":                                               #checks the course name and procede to fee
            if payment == "1":
                fee = 15000+500
            else:
                fee = 15000 - (15000*5/100)                             #if payment mode is card additional 500 charge apply or choose e-wallet to get 5% discount
        elif course == "2":
            if payment == "1":
                fee = 8000+500
            else:
                fee = 8000 - (8000*5/100)
        elif course == "3":
            if payment == "1":
                fee = 10000+500
            else:
                fee = 10000 - (10000*5/100)
        elif course == "4":
            if payment == "1":
                fee = 20000+500
            else:
                fee = 20000 - (20000*5/100)
        if course in "1234" and payment != '' and name!= '':                         #if users enters correct details a new tuple is created and append to studet_details list
            student_details.append((name,courses[int(course)-1],str(fee),payment))         
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
                print("        ",str(num)+".", " ".join(details[:len(details)-1]))
                print()
        choose_a_number = ''                                        #changes choose_a_number to empty to end infinite loop
    elif choose_a_number == "3":                                        #checks the selected number to perform delete operation
        ctr=0
        print("~"*20)
        print("        DELETE selected - Enter UserID to delete your details")
        print()
        userId = int(input('''Enter UserId
    Enter here > '''))
        
        if len(student_details) == 0 or userId > len(student_details):               #if details no found raises error
            print("*"*10)
            print("        No such details found in list to delete!")
            if len(student_details) ==0:
                choose_a_number = ''
        else:
            delete_details = student_details.pop(userId-1)                          #if details found delete the user details from the list
            print("\t",delete_details,"is deleted from the list")
            choose_a_number =''
    elif choose_a_number == "4":                                            #check selected number is match to perform edit operation
        ctr=0
        print("~"*20)
        print("        EDIT selected - Enter userId to edit details!")      #Indicates the user edit option is selected
        print()
        userId = int(input('''Enter userId
    Enter here> '''))                                                       #Asks user to enter userId to edit
        if len(student_details) == 0 or userId > len(student_details):
            print("*"*10)
            print("     No such details found in the list")                 #if entered details are wrong rises error
            if len(student_details) ==0:
                choose_a_number = ''
        else:                                       
            details = list(student_details[userId-1])
            what_to_update=input(''' Select:
    1 to update both payment & course,
    2 to update payment,
    3 to update course
    Enter here > ''')                                                   #Asks the user which has to edit
            if what_to_update == "1":                                   #If user selects both payment & course details it process
                print("~"*15)
                print("    Your are editing for", str(userId)+"."," ".join(details[:len(details)-1]))
                print()
                course = input('''
         Courses & Fees:
                1 to Python - 15000,
                2 to Java - 8000,
                3 to Ruby - 10000,
                4 to Rust - 20000
                
            Enter a new course >''')                                                  #Ask for course number
                payment = input('''
         payment mode:
                1.Card - 500RS/- Extra charge,
                2.E-Wallet - 5% Discount
            Enter paymode number > ''')                                               #Ask payment mode
                if course == "1":                                                     #checks the course name and procede to fee
                    if payment == "1":
                        fee = 15000+500
                    else:
                        fee = 15000 - (15000*5/100)                                   #if payment mode is card additional 500 charge apply or choose e-wallet to get 5% discount
                elif course == "2":
                    if payment == "1":
                        fee = 8000+500
                    else:
                        fee = 8000 - (8000*5/100)
                elif course == "3":
                    if payment == "1":
                        fee = 10000+500
                    else:
                        fee = 10000 - (10000*5/100)
                elif course == "4":
                    if payment == "1":
                        fee = 20000+500
                    else:
                        fee = 20000 - (20000*5/100)
                if course in "1234" and payment != '' and name!= '':                         #if users enters correct details a new tuple is created and append to studet_details list
                    student_details[userId-1] = (name,courses[int(course)-1],str(fee),payment)
                    print("        Your details are edited")
                    choose_a_number = ''
                else:
                    print("Wrong info please enter correct details")
            elif what_to_update == "2":                                                 #Checks user selected number to update the payment mode 
                print("~"*15)
                print("    Your are editing for", str(userId)+"."," ".join(details[:len(details)-1]))
                print()
                if "." in details[2]:
                    print("    Previously you selected E-wallet as payment, Recommended Card payment to update payment")
                else:
                    print("    Previously you selected Card as payment, Recommended E-wallet payment to update payment")
                payment = input('''
 payment mode:
        1.Card - 500RS/- Extra charge,
        2.E-Wallet - 5% Discount
        Enter paymode number > ''')
                if payment == "1":
                    if details[1] == "Python":                              #checks the course and update the pament mode according to user selected
                        details[2]= str(15000 +500)
                        ctr=1
                    elif details[1] == "Java":
                        details[2] = str(8000 + 500)
                        ctr=1
                    elif details[1] == "Ruby":
                        details[2] = str(10000+500)
                        ctr=1
                    elif details[1] == "Rust":
                        details[2] = str(20000+500)
                        ctr=1
                else:
                    if details[1] == "Python":
                        details[2]= str(15000 -(15000*5/100))
                        ctr=1
                    elif details[1] == "Java":
                        details[2] = str(8000 -(8000*5/100))
                        ctr=1
                    elif details[1] == "Ruby":
                        details[2] = str(10000 -(10000*5/100))
                        ctr=1
                    elif details[1] == "Rust":
                        details[2] = str(20000 -(20000*5/100))
                        ctr=1
                if ctr != 0:
                    student_details[userId-1] = tuple(details)
                    print("\t","Details are updated!")
                    choose_a_number=''
            elif what_to_update == "3":                                             #Checks user selected input with course option to update course
                print("~"*15)
                print("    Your are editing for", str(userId)+"."," ".join(details[:len(details)-1]))
                print()
                course = input('''
         Courses & Fees:
                1 to Python - 15000,
                2 to Java - 8000,
                3 to Ruby - 10000,
                4 to Rust - 20000
                
            Enter a new course >''')
                if course == "1":                                                   #checks the course and update the payment according to it
                    details[1]= "Python"
                    if "." in details[2]:                                           #if . in fee then it is float and payment is updated accounding to e-wallet
                        details[2] = str(15000 - (15000*5/100))
                    else:
                        details[2]= str(15000+500)                                  #if there is no . in fee then fee is updated according to card payment mode
                    ctr=1
                elif course == "2":
                    details[1]= "Java"
                    if "." in details[2]:
                        details[2] = str(8000 - (8000*5/100))
                    else:
                        details[2]= str(8000+500)
                    ctr=1
                elif course == "3":
                    details[1]= "Ruby"
                    if "." in details[2]:
                        details[2] = str(10000 - (10000*5/100))
                    else:
                        details[2]= str(10000+500)
                    ctr=1
                elif course == "4":
                    details[1]= "Rust"
                    if "." in details[2]:
                        details[2] = str(20000 - (20000*5/100))
                    else:
                        details[2]= str(20000+500)
                    ctr=1
                if ctr != 0:
                    student_details[userId-1] = tuple(details)
                    print("\t","Details are updated!")
                    choose_a_number=''
                    
    elif choose_a_number == "5":                                #checking the selected number is 5 to continue the filter process
        print("~"*25)
        print("        FILTER selected")                        #Indicates filter is selected
        choose_filter=input('''choose:
    0 to filter with Course,       
    1 to filter with Payment mode
    Enter here > ''')                                           #Asks users to select the filter method to filter the data 0 for course, 1 for payment mode
        if choose_filter == "0":                                #Checking selection filter method is Course of not
            print("-"*20)
            print("        Selected Course as filter option")
            choose_course = int(input('''Chose:
    1 to filter with Python course,
    2 to filter with Java course,
    3 to filter with Ruby course,
    4 to filter with Rust course
    Enter here > '''))                                          #Asks the user on which course it has to filter
            print("~"*60)
            for i in student_details:
                if courses[choose_course -1] in i:              #checks the user selected course and prints the output
                    print("\t"," ".join(list(i)))
            print("        Filtered by {} course".format(courses[choose_course - 1]))
            choose_a_number =''
        elif choose_filter == "1":                                          #checks the if user selected payment mode as filter
            print("-"*20)
            print("        Selected Payment mode as filter option")
            choose_payment_mode=input('''Choose:
    1 to Filter with Card payment mode,
    2 to Filter with E-wallet payment mode
    Enter here > ''')                                                       #Asks user to select Card or E-wallet as Filter
            print("~"*60)
            for i in student_details:
                if choose_payment_mode == i[3]:              #checks data is matched with Card payment mode or not
                    print("\t"," ".join(list(i[:len(i)-1])))
                elif i[3] == choose_payment_mode:
                    print("\t"," ".join(list(i[:len(i)-1])))                           #checks data is matched with Card payment mode or not and prints
            print("        Filtered by {} payment method".format(pym[int(choose_payment_mode)-1]))
            choose_a_number =''             #clears the choose_a_number to ask choice again 

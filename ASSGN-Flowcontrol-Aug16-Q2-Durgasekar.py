"""
A student has joined a course costing as per the given table. If the fee is paid via card, an additional service charge of Rs. 200/- is added
but if payment is made through e-wallet, a discount of 5% is given for the payment. Use this reference table

_____
python : 15000 |
java   : 8000  |
ruby   : 10000 |
rust   : 20000 |
_____|
Complete the program to: Accept the Student name, course and mode of payment and Print the fee for the student. 
"""



courses =["python","java","ruby","rust"]                #course names in a list

course =input('''Choose course
1 to choose Python,
2 to choose Java,
3 to choose Ruby,
4 to choose Rust
Enter here > ''')                                        #Ask user choose course
student_name = input("Enter student name > ")            #Asks user to  enter name
fee =0                                                  #default fee is 0
payment_mode = input('''Enter a payment mode number
1 to choose Card,
2 to choose E-wallet> ''')                               #Ask user to select payment mode 1 for card, 2 for e-wallet


if course == "1":                                       #checking selected course
    if payment_mode == "1":                             #check payment through card or not
        fee = 15000+200
    elif payment_mode == "2":
        fee = 15000 - (15000*5/100)
elif course == "2":                                     #checking selected course
    if payment_mode == '1':                             #check payment through card or not
        fee = 8000+200                                  #calculate fees according to course selected and payment mode
    elif payment_mode == '2':
        fee = 8000 - (8000*5/100)
elif course == "3":                                     #checking selected course
    if payment_mode == '1':                             #check payment through card or not
        fee = 10000+200                                 #calculate fees according to course selected payment mode
    elif payment_mode == '2':
        fee = 10000 - (10000*5/100)
elif course == "4":                                     #checking selected course
    if payment_mode == '1':                             #check payment through card or not
        fee = 20000+200                                 #calculate fees according to course selected payment mode
    elif payment_mode == '2':
        fee = 20000 - (20000*5/100)

if course in "1234" and payment_mode in "12" and student_name != '':                                           #printing student details and fee details
    print(student_name, "joined for", courses[int(course)-1], "course & fee is", fee)
else:
    print("Unrecognized course or payment mode or name!!")                         #print if error

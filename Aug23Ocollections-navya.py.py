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
Accept a Student name, course and mode of payment 
Print the fee for the student.
Accept details of multiple students
Ask the user if they need to exit the application and then stop
'''
ans = "y"
while 1:
    if ans == "y":                                                          #checks the users decision
        name = input("Enter your name >")                                   #asks user's name
        course = input("Enter course you want to learn >")                  #Asks course user wants to learn
        payment = input("Choose payment mode card: 1, e-wallet: 2 >")       #Aks the payment method
        
        if course == "python":                                              #check selected course
            if payment == "1":                                              #if payment method is card 500 extra charge, if it is e-wallet 5% discount
                fee =15000+500
            else:
                fee = 15000-(15000*5/100)
        elif course == "java":                                              #check selected course
            if payment == "1":
                fee = 8000+500
            else:
                fee = 8000-(8000*5/100)
        elif course == "ruby":                                              #if payment method is card 500 extra charge, if it is e-wallet 5% discount
            if payment == "1":
                fee = 10000+500
            else:
                fee = 10000-(10000*5/100)
        elif course == "rust":                                              #check selected course
            if payment == "1":
                fee = 20000+500                                             #if payment method is card 500 extra charge, if it is e-wallet 5% discount
            else:
                fee = 20000-(20000*5/100)
        if course != '' and fee >0 and name!='':
            print(name, "selected the", course,"course & it's fee is", fee)             #prints the user's name, selected course and it's fee
            ans = input("Choose y to continue to add another course or n to quit >")    #Ask user is he willing to add another course or not
        else:
            print("Missing name or course or payment mode selection, please enter again")
    else:
        break                                                                       #if user selected no the loop breaks


'''
2.Question
Ask the user to enter userName
If the userName is wrong (not 'admin'), then ask the user to enter the user name again
If userName=='admin' then ask the user to enter password
If password is wrong, repeat the process
If password=='admin123' then greet the user and end the program
'''

while 1:
   username = input("Enter user name>")                     #Asks username
   if username == "Navya":                              #if correct asks password or again ask username
       password = input("Enter your password >")            #if password is correct it greets and break loop or ask details again
       if password == "Navya1234":
           print("Hello",username, "hai")
           break
       else:
           print("Wrong password")

'''
Code based assessment
````
3.	Question
Generate the pattern: 
	5555555555 
	44444444 
	333333 
	2222 
	11
	0
'''
num = int(input("Enter a number >"))            #ask user to enter a number
while num >=0:
    if num!=0:                                  #checks num is not equal to 0 so it prints munlitple string values
        print(str(num)*num*2)
    else:                                       #if num is 0 it prints zero
        print(0)
    num-=1
        

'''

4.	Question
msg = 'Hello world, Python people!'
Write the required statement to display:
a.	'World'
b.	' Python people'
c.	' Python world'
d.	' Hello people'
e.	' Hello people who belong to Python world'
f.	'Hello world, Python people'
g.	'elpoep nohtyP ,dlrow olleH'
h.	'olleH'
i.	'elpoep'
j.	'nohtyP dlrow'
'''

msg = 'Hello world, Python people!'
print(msg[6:11].capitalize())                    #a
print(msg[12:26])                   #b
print(msg[12:19]+" "+msg[6:11])     #c
print(" "+msg[:5]+msg[19:26])       #d
print(" "+msg[:5]+msg[19:26]+" Who belongs to"+msg[12:19]+msg[5:11])        #e
print(msg[:26])                                                             #f
print(msg[-2::-1])                                                          #g
hello_rev = msg[:5]
print(hello_rev[::-1])                                                      #h
people_rev = msg[19:26]                                                     #take values and reveses it
print(people_rev[::-1])                                                     #i
final_rev = msg[6:11]+" "+msg[12:19]                                      #take values and reveses it
print(final_rev[::-1])                                               #j



'''
5.Question
Write a program that generates the block shown below.

123456789 - Sum of the characters minus the last character is:36
234567891 - Sum of the characters minus the last character is:44
345678912 - Sum of the characters minus the last character is:43
456789123 - Sum of the characters minus the last character is:42
567891234 - Sum of the characters minus the last character is:41
678912345 - Sum of the characters minus the last character is:40
789123456 - Sum of the characters minus the last character is:39
891234567 - Sum of the characters minus the last character is:38
912345678 - Sum of the characters minus the last character is:37
'''
ctr = 0
input_line = '123456789'
while ctr < len(input_line):                                                    #while loop for input it breaks untill the ctr value equal to len(input)
    result=0
    changes_num = input_line[ctr:]+input_line[:ctr]                             #using string slicing the input is updated for each loop
    ctr2=0                                                      
    while ctr2 < len(changes_num)-1:                                            #Another while loop for to sum the input except last character
        result+=int(changes_num[ctr2])
        ctr2+=1                                                                 #condition to break nested while loop
    print(changes_num,"- Sum of the characters minus the last character is:",result)      #print the sum of input except last character
    ctr+=1   





                                                                   #condition to break main while loop

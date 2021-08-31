''' A student has joined a course costing as per the given table. If the fee is paid via card,
an additional service charge of Rs. 500/- is added but if payment is made through e-wallet,
a discount of 5% is given for the payment. Use this reference table :
_______________
python : 15000 |
java   : 8000  |
ruby   : 10000 |
rust   : 20000 |
_______________|
Complete the program to: Accept the Student name, course and mode of payment and Print the fee for the student. '''


student=input("Enter the Student's name > ")
course=input("Enter the course for the student > ")
payment=input(
'''Enter the payment mode as:
1 for card
2 for e-wallet
> ''')

fee=0
if course == 'python':
    if payment=='1':
	    fee=15000+500
    elif payment=='2': 
	      fee=15000-(15000*5/100)
elif course == 'java':
    if payment=='1':
            fee=8000+500
    elif payment=='2': 
	      fee=8000-(8000*5/100)
    
elif course == 'ruby':
    if Payment=='1':
            fee=10000+500
    elif payment=='2': 
	      fee=10000-(10000*5/100)
    
elif course == 'rust':
    if payment=='1':
            fee=20000+500
    elif payment=='2': 
	      fee=20000-(20000*5/100)
  
if course in 'python,java,ruby,rust' and fee > 0:
    print(student, 'joined for', course, 'course & Fee is', fee)
else: print('unrecognized course or payment mode !!')

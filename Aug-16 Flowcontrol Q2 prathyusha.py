'''A student has joined a course costing as per the given table. If the fee is paid via card, an additional service charge of Rs. 200/- is added but if payment is made through e-wallet, a discount of 5% is given for the payment. Use this reference table :
_______________
python : 15000 |
java   : 8000  |
ruby   : 10000 |
rust   : 20000 |
_______________|
Complete the program to: Accept the Student name, course and mode of payment and Print the fee for the student. '''


student=input("enter the student's name:")
course=input("enter the course:")
payMode=input('''Enter the payment mose as: 1 for card 2 for e-wallet:''')

fee=0
if course in'python':
	if payMode=='1':
		fee=15000+200
	elif payMode=='2':
		fee=15000-(15000*5/100)
elif course in 'java':
	if payMode=='1':
		fee=8000+200
	elif payMode=='2':
		fee=8000-(8000*5/100)
elif course in 'ruby':
	if payMode=='1':
		fee=10000+200
	elif payMode=='2':
		fee=10000-(10000*5/100)

elif course in 'rust':
	if payMode=='1':
		fee=20000+200
	elif payMode=='2':
		fee=20000-(20000*5/100)

if course in 'python,java,ruby,rust' and fee>0:
	print(student,'joined for',course,'course & fee is', fee)
else:
	print('unrecognized course or payment mode!')

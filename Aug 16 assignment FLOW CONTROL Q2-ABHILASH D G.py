"""
1:
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
"""
while 1:
 name=input("enter the name")
 if name!='Quit':
  
  course=input("enter the course")
  paymode=input("enter the mode of payment")
  fee=0
  if course in 'python':
    if payMode=='1': 
     fee=15000+200
    elif payMode=='2': 
     fee=15000-(15000*5/100)
  elif course in 'java':
   if paymode== '1':
     fee=8000+200
   elif paymode=='2':
     fee=8000-(8000*5/100)
  elif course in 'ruby':
     if paymode== '1':
       fee=10000+200
     elif paymode=='2':
        fee=10000-(10000*5/100)
  elif course in 'rust':
     if paymode== '1':
       fee=20000+200
     elif paymode=='2':
        fee=20000-(20000*5/100)
  if course in 'python,java,ruby,rust' and fee > 0:
   print(name, 'joined for', course, 'course & Fee is', fee)
  else:
   print('unrecognized course or payment mode !!')
        
 else:
     break

""" 2: Question
Ask the user to enter userName
If the userName is wrong (not 'admin'), then ask the user to enter the user name again
If userName=='admin' then ask the user to enter password
If password is wrong, repeat the process
If password=='admin123' then greet the user and end the program
"""
while True:
    name=input("enter user name")  #username
    if name=="admin":    #  if username is equal to admin
        paass=input("enter password")
        if paass=="admin123":
          print("hiii",name,paass)
          break

"""
3: Question
Generate the pattern: 
	5555555555 
	44444444 
	333333 
	2222 
	11
	0"""
c=5
n=1
while n<c:  #id n is less than c then this follwing statement will execute
    while c>=1:
        print(str(c)*c*2)  #prints the output
        c=c-1
        continue
    n=n+1
    break

"""
 4: Question
msg = 'Hello world, Python people!'
Write the required statement to display:
'World'
' Python people'
' Python world'
' Hello people'
' Hello people who belong to Python world'
'Hello world, Python people'
'elpoep nohtyP ,dlrow olleH'
'olleH'
'elpoep'
'nohtyP dlrow'
"""
msg='Hello world, Python people!'
print(msg[6:11].title()) #'World'
print(msg[13:26])   #' Python people'
print(msg[13:19],msg[6:11])  #' Python world'
print(msg[0:5],msg[20:26])   #' Hello people'
print(msg[0:5],msg[20:26],'who belong to',msg[13:19],msg[6:11])    #' Hello people who belong to Python world'
print(msg[0:26])   #'Hello world, Python people'
print(msg[-2::-1])  #'elpoep nohtyP ,dlrow olleH'
print(msg[-22::-1])   #'olleH'
print(msg[-2:19:-1])  #'elpoep'
print(msg[-9:5:-1])   #'nohtyP dlrow'

"""
5: Write a program that generates the block shown below.
123456789 - Sum of the characters minus the last character is:36
234567891 - Sum of the characters minus the last character is:44
345678912 - Sum of the characters minus the last character is:43
456789123 - Sum of the characters minus the last character is:42
567891234 - Sum of the characters minus the last character is:41
678912345 - Sum of the characters minus the last character is:40
789123456 - Sum of the characters minus the last character is:39
891234567 - Sum of the characters minus the last character is:38
912345678 - Sum of the characters minus the last character is:37
"""
name=[1,2,3,4,5,6,7,8,9]
l=0
while l<len(name): # checks the length of name
    n=name[l:]+name[:l]
    print(n,"sum of all numbers minus the last number:",45-n[-1]) #prints by suming the sequence and minus of last number
    l+=1

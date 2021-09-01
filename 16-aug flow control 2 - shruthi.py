"""A student ha joined a costing as per the given table. If the fee is paid via card , an aditional service of rs 200/- is added but if payment is made
through e-wallet , a discount of 5% is given for the payment .
python-15000
java-8000
ruby-10000
rust-20000
complete the program to accept the student name , course and mode of payment and print the fee for the student."""



n=input("enter the student name: ")
c=input("""enter the course name
python/java/ruby/rust: """)
p=input("enter the payment more 1.card/2.e-wallet: ")
total=0
if c=="python":
    if p == "1":
        total=15000+200
    else:
        total=15000-(15000*5/100)
elif c=="java":
    if p == "1":
        total=8000+200
    else:
        total=8000-(8000*5/100)
elif c=="ruby":
    if p == "1":
        total=10000+200
    else:
        total=10000-(10000*5/100)
elif c=="rust":
    if p == "1":
        total=20000+200
    else:
        total=20000-(20000*5/100)

if c in 'python,java,ruby,rust' and total>0:
    print("Student-",n,"registered for the course-",c,"for the amount-Rs:",total)
else:
    print("please enter a valid payment /course")




    
        

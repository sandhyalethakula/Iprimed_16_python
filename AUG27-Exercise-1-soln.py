"""
MAKE A CONTACT LIST IN MEMORY::
1. COLLECT SOME VALID DATA ABOUT A PERSON AND STORE IT AS A DICT.
      NAME (fn,ln,ins),
      PHONE NUMBER,
      DATE OF BIRTH (d,m,y)
2. AND STORE THIS DICT IN A LIST.
3. PRINTS THE ENTERED INFORMATION.

ASSIGNMENT-A:
DO WHAT IS REQUIRED TO BE DONE ??
1. WRITE COMMENTS FOR EACH STATEMENT AS PER YOUR UNDERSTANDING
2. Write a loop to collect data about minimum 5 ppl

CONDITIONS:
# Date entered is to be numeric (dd,mm,yyyy)
# Age of person - 15+  upto+ 75 years
# DOB to be printed as  12/Jan/2001
# Phone number: numeric, 10 digit
"""

#2. AND STORE THIS DICT IN A LIST. 
contacts = [] 

ctr=65       #counter for default dummy data if user does not enter data - 65=character'A'

# Month data to validate & print
months={1:(31,'Jan'), 2:(28,'Feb'), 3:(31,'Mar'), 4:(30,'Apr'), 5:(31,'May'), 6:(30,'Jun'),
        7:(31,'Jul'), 8:(31,'Aug'), 9:(30,'Sep'), 10:(31,'Oct'), 11:(30,'Nov'), 12:(31,'Dec'),}

# loop to collect contacts
while 1:
    print('Contact Info - Enter data as prompted')
    print('*'*40,'\n')
    #1. COLLECT SOME VALID DATA ABOUT A CONTACT PERSON AND STORE IT IN MEMORY AS A DICT.
    contact = {'name':{'fn':'','ln':'','in':''},'ph':'','dob':{'dd':0,'mm':'', 'yy':0}}

    # collect name info ---------------------------------------------------
    while 1:        
        fn=input('Enter First name > ') or 'firstName'+chr(ctr)
        ln=input('Enter last name > ')  or 'lastName'+chr(ctr)
        initials=input('Enter initials(max 2) > ')  or 'x'
        if fn.isalpha() and ln.isalpha()and initials.isalpha() and len(initials)<=2:
            break
        else:
            print('invalid entry. Re-enter')

    contact['name']['fn']=fn
    contact['name']['ln']=ln
    contact['name']['in']=initials 

    # collect ph info-------------------------------------------
    while 1:
        ph=input('Enter phone number > ') or '000000000'+str(ctr-64)
        if ph.isnumeric() and len(ph)==10:
            break
        else:
            print('invalid entry. Re-enter')            

    contact['ph']=ph

    # collect dob info-------------------------------------------
    while 1:
        yy=input('Enter valid year - 1946 to 2006 > ')  or '2000'
        #validate
        if yy.isnumeric():
            yy=int(yy)
            if yy>=1946 and yy<=2006:break        

    while 1:
        mm=input('Enter valid month as a number > ')  or '5'
        #validate
        if mm.isnumeric():
            mm=int(mm)
            if mm>=1 and mm<=12:break        

    while 1:        
        dd=input('Enter valid day as number > ') or '1'
        #validate
        if dd.isnumeric():
            dd=int(dd)
            if dd>=1 and dd<=months[mm][0]:break

    contact['dob']['dd']=dd
    contact['dob']['mm']=months[mm][1]
    contact['dob']['yy']=yy    

    # End of data entry-------------------------------------    

    contacts.append(contact)    # Save newly entered data to contacts list
    del contact                 # delete from memory and re-initialize at the start of the loop
    ctr+=1      # counter for the default dummy data

    # end the data collection loop
    if len(contacts)>=3:
        if input('Do you want to quit? > y/n or just press enter >') in 'yY':break
        
#---------------------------------------------------------------------------------------
#3. PRINTS THE ENTERED INFORMATION.
for i in contacts:print(i)

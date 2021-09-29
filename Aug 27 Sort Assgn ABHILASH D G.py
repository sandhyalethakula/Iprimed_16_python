"""COLLECT INFORMATION ABOUT A CONTACT: 
fullname, phoneNumber, Birthday-Month & Day

DISPLAY THE COLLECTED CONTACTS IN THE SORTED ORDER OF BIRTHDAY
IF 2 CONTACTS HAVE THE SAME BIRTHDAY, ORDER THEM IN THE ASCENDING ORDER OF PHONE NUMBER"""


contacts=[]
ctr=65
months={1,2,3,4,5,6,7,8,9,10,11,12}
while 1:
    
    while 1:
        print('Contact Info - Enter data as prompted')
        print('*'*40,'\n')
        
         
        contact = {'name':'','ph':'','dob':{'dd':0,'mm':0}} #creating the empty dictionary
        break

    
    while 1:        
        fn=input('Enter Full  name > ') or 'full Name'+chr(ctr)
        
        if fn.isalpha() : #checking whether the entered name is alphabet or not
            break
        else:
            print('invalid entry. Re-enter')

    contact['name']=fn #storing the data in dictionary
    
    

    while 1:
        ph=input('Enter phone number > ') or '000000000'+str(ctr-64)
        if ph.isnumeric() and len(ph)==10:
            break
        else:
            print('invalid entry. Re-enter')            

    contact['ph']=ph

    
#taking minth from user and validating
    while 1:
        mm=input('enter valid month as a number > ')  or '5'
        if mm.isnumeric():
            mm=int(mm)
            if mm>=1 and mm<=12:break
    #taking day and validating
    while 1:
        dd=input('enter valid day as number>')or '1'
        if dd.isnumeric():
            dd=int(dd)
            if dd>=1 and dd <=mm:break
    contact['dob']['dd']=dd
    contact['dob']['mm']=mm
    


    contacts.append(contact)
    del contact
    ctr+=1

    if len(contacts)>=3:  #if contacts is greater than 3 it will print do u want to enter or quit
        if input('do you want to quit?>y/n or just press enter>') in 'yY':break
for i in contacts:print(i)   #prints all the contacts 


sorts= contacts #assigning contacts to sorts
def persons(person):   #defining the class 
    return ((person['dob']['mm'],person['dob']['dd']),int(person['ph']))

sorts.sort(key=persons) #sorting the lists using sort method
for i in sorts:  #for multiple values doing sort
    print(i['name'],i['ph'],i['dob'])


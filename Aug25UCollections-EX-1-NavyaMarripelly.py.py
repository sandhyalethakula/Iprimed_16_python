'''WHAT DOES THIS PROGRAM DO ??
MAKE A CONTACT LIST IN MEMORY::
1. COLLECT SOME VALID DATA ABOUT PEOPLE AND STORES IT AS A DICT.
      NAME (fn,ln,ins),
      PHONE NUMBER,
      DATE OF BIRTH (d,m,y)

2. AND STORE THIS DICT IN A LIST.
3. PRINTS THE ENTERED INFORMATION.
4. PRINTS THE CONTACTS WHOSE BIRTHDAYS FALL IN THE CURRENT MONTH
--------------------------------
ASSIGNMENT-A:
WHAT IS REQUIRED TO BE DONE ??
1. WRITE COMMENTS FOR EACH STATEMENT AS PER YOUR UNDERSTANDING
2. Write a loop to collect data from 20 ppl
3. Get a month from the user &
      filter persons having birthdays in the entered month & print
---------------------------------
'''
#IMPL
#1.
mts={1:31,2:28,3:31,4:30}


ppl=[]   #list of entered contacts


# COLLECT INFO FROM USER 3 TIMES
for i in range(3):
   # each contact's template is created for every iteration
   # to add the newly entered data
   personData={'fullname' : {'fn':'',
                           'ln':'',
                           'ins':''},
               'ph':'',
               'dob' : {'d':'',
                     'm':'',
                     'y':''}  
               }
   # collect info .... (loop & validate)
   fn=input('FirstName > ')
   ln=input('LastName > ')
   ins=input('Initials > ')

   ph=input('Phone Number > ')

   d=input('Day of DOB > ')
   m=input('month of DOB > ')
   y=input('year of DOB > ')


   # entered data is assigned to the template
   personData['fullname']['fn']=fn
   personData['fullname']['ln']=ln
   personData['fullname']['ins']=ins
   personData['ph']=ph
   personData['dob']['d']=d
   personData['dob']['m']=m
   personData['dob']['y']=y

   # person data is appended to the list of entered ppl
   ppl.append(personData)
   # contact's template is deleted to remove the old data
   del personData
   
#-------------------------------------END OF DATA ENTRY----------------------

#input()
print('-'*70)   
print()
print('You entered: ... ')
print()

# print each contact's info
for person in ppl:
   for attr in person:
      print(attr, person[attr])
   print('-'*40)
print()

input()  
#------------------

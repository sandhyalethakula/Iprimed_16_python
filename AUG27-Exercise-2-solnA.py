'''
CREATE A DICTIONARY OF STUDENTS TAKING AUTOMATED TRAINING:
    1. Each student has: id, fullName, course, joinedOn, completesOn
    2. Collect valid data for: fullName, course, joinedOn
    3. The Date of completion has to be calculated based on the course data.
    4. The ID has to be generated as a running number
 
AS SUPPORT, CREATE A COURSES OPTIONS:
    courses are: PYML, PythonML, 10 weeks;
                 PYDS, PythonDS, 8 weeks;
                 PYWA, PythonWA, 6 weeks;
                 
COLLECT MULTIPLE STUDENTS INFO (min=3) AND STORE.
PRINT THE STUDENTS COLLECTED WHEN THE APPLICATION IS ENDED
USE DEFAULT DATA F0R QUICK DATA ENTRY
'''
courses={'PYML':('PythonML',10),'PYDS':('PythonDS',8),'PYWA':('PythonWA',6)}
# STORE THIS STUDENTS IN A LIST. 
students = []

ctr=65       #counter for test data if user does not enter data - 65=character'A'
id_num = 1

# Month data to validate & print
months={1:(31,'Jan'), 2:(28,'Feb'), 3:(31,'Mar'), 4:(30,'Apr'), 5:(31,'May'), 6:(30,'Jun'),
        7:(31,'Jul'), 8:(31,'Aug'), 9:(30,'Sep'), 10:(31,'Oct'), 11:(30,'Nov'), 12:(31,'Dec'),}

# loop to collect students
while 1:
    print('student Info - Enter data as prompted\n')
    #1. COLLECT SOME VALID DATA ABOUT A PERSON AND STORE IT AS A DICT.
    student = {'id':0,'name':{'fn':'','ln':'','in':''},'crs':'','doj':{'dd':0,'mm':'', 'yy':0},'doc':'ToBeCalc'}

    # ID: ------------id to be generated---------------------------------------
    student['id']=id_num
    # NAME:-----------collect name info----------------------------------------
    while 1:        
        fn=input('Enter First name > ') or 'firstName'+chr(ctr)
        ln=input('Enter last name > ')  or 'lastName'+chr(ctr)
        initials=input('Enter initials(max 2) > ')  or 'x'
        if fn.isalpha() and ln.isalpha()and initials.isalpha() and len(initials)<=2:
            break
        else:
            print('invalid entry. Re-enter')

    student['name']['fn']=fn
    student['name']['ln']=ln
    student['name']['in']=initials 

    # CRS:-------------collect course info-------------------------------------------
    while 1:
        crs=input('Enter course > ') or 'PYML'
        if crs in courses:
            break
        else:
            print('invalid entry. Re-enter')            

    student['crs']=crs

    # DOJ:----------collect doj info-------------------------------------------
    yy='2021'     

    while 1:
        mm=input('Enter valid month as a number. Either July or August > ')  or '8'
        #validate
        if mm.isnumeric():
            mm=int(mm)
            if mm in (7,8):break        

    while 1:        
        dd=input('Enter valid day as number: should be any of last 45 days or today > ') or '26'
        #validate
        if dd.isnumeric():
            dd=int(dd)
            if mm==7:
                if dd>=12 and dd<=31:break
            elif mm==8:
                if dd>=1 and dd<=26:break

    student['doj']['dd']=dd
    student['doj']['mm']=months[mm][1]
    student['doj']['yy']=yy    

    # DOC:-----------calc date of completion-------------------------------
    student['doc']='ToBeCalc'

    # End of data entry----------------------------------------------------    

    students.append(student)    # Save newly entered data to students list
    del student                 # delete from memory and re-initialize at the start of the loop
    ctr+=1      # counter for the test data
    id_num+=1
    # end the data collection loop
    if len(students)>=3:
        if input('Do you want to quit? > y/n or just press enter >') in 'yY':break
        
#```````````````````````````````````````````````````````````````````````````````````````````````````````````
        
#3. PRINTS THE ENTERED INFORMATION.
for i in students:print(i)



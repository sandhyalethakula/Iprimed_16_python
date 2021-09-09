'''
Create a dictionary of students taking automated training:
    1.Each sudent has: id, fullname, course, joindeOn, completesOn
    2. Collect valid data for: fullname, course, joinedOn => -45 days to 26/Aug/2021
    3.The date of completion has to be calculated based on the course data and added automatically
    4.The Id has to be generated as a running numbers (...first entru => id ==1, etc)
Create a course options:
    courses are: PYML, PYTHONML, 10 WEEKS,
                 PYDS, PYTHONDS, 8 WEEKS,
                 PYWA, PYTHONWA, 6 WEEKS
collect multiple students info (min=3) and store.
print the students collected when the application is ended
default data for quick data entry
'''
user_details=[]             #empty user list
months={1:(31,'Jan'), 2:(28,'Feb'), 3:(31,'Mar'), 4:(30,'Apr'), 5:(31,'May'), 6:(30,'Jun'),
        7:(31,'Jul'), 8:(31,'Aug'), 9:(30,'Sep'), 10:(31,'Oct'), 11:(30,'Nov'), 12:(31,'Dec'),}     #month details in dictionary
courses={'1':('PYML', 'PythonMl', '10 weeks'),'2':('PYDS', 'PythonDS', '8 weeks'),'3':('PYWA', 'PythonWA', '6 weeks')}  #course details in dictonary
while 1:
    #for each loop an empty details of dictionary is created
    user_dict ={"id":'',"name":{'first name':'','last name':'', "initial":''},"course":{'course name':'', 'duration':''},"joinedOn":{"dd":'','mm':'','yy':2021},"completedOn":{'dd':'',"mm":'',"yy":2021}}
    while 1:
        print("~"*30)
        print("-"*10,"User Details collection","-"*10)
        first_name = input("Enter first name > ") or "firstname"
        last_name = input("Enter last name > ") or "lastname"                       #ask first,last,initial names of user or takes default values
        initial = input("Enter initial in one letter max(2 letters) > ") or "X"
        if first_name.isalpha() and last_name.isalpha() and len(initial) <= 2 and initial.isalpha():        #if user entered details are alphabets conditon checks
            user_dict["name"]["first name"]=first_name.title()
            user_dict["name"]['last name']=last_name.title()            #user details stroed in name in a user_dict dictionary
            user_dict["name"]['initial']=initial.title()
            break
        else:
            print("*"*30)
            print("Invalid entry input should be in alphabets!")        #if invalid input error raises
   
    while 1:
        month=input("Enter joined month between July to August > ") or '7'     #takes month of joined from user it should be between july and agust
        if month.isnumeric():
            month = int(month)
            if month > 0 and month >=7 and month <=8:               #checks month is between july and agust
                break
            else:
                print("*"*30)
                print("Invalid entry months shoulld between July to August")
        else:
            print("*"*30)                                           #if month is not numeric raise error
            print("Invalid entry enter in numeric format ")
    user_dict["joinedOn"]['mm']= month                              #month is stored in mm in joinedOn in user_dict
    while 1:
        day=input("Enter joined day > ")  or '12'      #takse joined day from user
        if day.isnumeric():
            day = int(day)
            if month == 7 and day >=12 and day<= 31:        #if month is july it should be starts from 12 and day should not exceed 31
                break
            elif month ==8 and day >0 and day<= 26:         #if month is july the day stats from 1 and ends with 26
                break
            else:
                print("*"*30)
                print("Invalid entry, Day should between July 12 to August 26!")    #if entered day is not between july 13 to 31 or august 1 to 26 days the it raises errro
        else:
            print("*"*30)
            print("Invalid entry enter again!")         #if entered day is not numeric raises error
    user_dict["joinedOn"]['dd']= day                    #day is stored in dd in joinedOn in user_dict 

    while 1:
        select_course = input('''Enter course
        1 to PYML, PythonMl, 10 weeks,
        2 to PYDS, PythonDS, 8 weeks,
        3 to PYWA, PythonWA, 6 weeks
        Enter here >''') or "1"                           #ask user to select course
        month_r=0               #reffers final month of the course
        final =0                #reffers final day of the course
        if select_course.isnumeric():                   #checks user enter course number is numeric or not
            day_join =int(user_dict["joinedOn"]['dd'])  #takse day of joined month
            if select_course == "1":                                #checks select_course matches with 1
                joined_month = user_dict["joinedOn"]['mm']          #takes joined month 
                ctr=1                                               #ctr adds +1 for each loop to increase the month
                days_of_selected_month = months[int(joined_month)][0]       #days of a joined month
                remaining_days = days_of_selected_month - day_join          #days of joined month - day of joined month ex: 31 - 13
                total_days = remaining_days                                 #total_days is remaining days in month ex: 31-13 = 18
                for i in range(5):
                    month_r = int(joined_month)+ctr                         #month_r to calculate the months 
                    next_month = months[int(joined_month)+ctr][0]           #after adding ctr new month details are output
                    remaining_days = next_month                             #remaining_days is new month days
                    total_days += remaining_days                            #total_days is added with new month days
                    if total_days == 70:
                        final = remaining_days
                        break
                    elif total_days > 70:                                   #if total_days greather than duration days
                        final = remaining_days -(total_days-70)             #days of month - (total_days - duration days)
                        break                                               #break 
                    ctr+=1                                                  #ctr+=1 for each loop

                    
            #The above process is same for the remaining courses duration calculation
            elif select_course == "2":
                joined_month = user_dict["joinedOn"]['mm']
                ctr=1
                days_of_selected_month = months[int(joined_month)][0]
                remaining_days = days_of_selected_month - day_join
                total_days = remaining_days
                for i in range(5):
                    month_r = int(joined_month)+ctr
                    next_month = months[int(joined_month)+ctr][0]
                    remaining_days = next_month
                    total_days += remaining_days
                    if total_days == 56:
                        final=remaining_days-1
                        break
                    elif total_days > 56:
                        final =remaining_days -(total_days-56)
                        break
                    ctr+=1
            elif select_course == "3":
                joined_month = user_dict["joinedOn"]['mm']
                ctr=1
                days_of_selected_month = months[int(joined_month)][0]
                remaining_days = days_of_selected_month - day_join
                total_days = remaining_days
                for i in range(5):
                    month_r = int(joined_month)+ctr
                    next_month = months[int(joined_month)+ctr][0]
                    remaining_days = next_month
                    total_days += remaining_days
                    if total_days == 42:
                        final=remaining_days-1
                        break
                    elif total_days > 42:
                        final = remaining_days -(total_days-42)
                        break
                    ctr+=1
            user_dict["completedOn"]['dd']=final-1
            user_dict["completedOn"]['mm'] =month_r                             #day,month,course name,duration,id is stored in user_dict
            user_dict['course']['course name']= courses[select_course][1]
            user_dict['course']['duration']= courses[select_course][2]
            user_dict["id"]=len(user_details)+1
            user_details.append(user_dict)                                  #created dictionary is appended to user_details list
            del user_dict                                   #delete the dictionary data to not overwrite the old data with new data
        else:
            print("Enter valid input!")         #if user doesn't enter anything error raises
        if final !=0:                           #after successful creation loop breaks
            break
    if len(user_details) >=3:                       #after 3 successful creation dictionary ask the user to continue or quit
        if input("Do you want to Quit ? y or n > ") in "yY":            #if user select yes  entire loop breaks
            break
print("~"*50)
print("\t","\t", "Final result")
for i in user_details:              #After main loop breaks each dictionary in user_details are printed 
    data=i
    print("ID {}. Name: {} {} {}  Course: {}  joinedOn: {}/{}/{}  completedOn: {}/{}/{} Duration: {}".format(data['id'],data["name"]['initial'],data["name"]['first name'],data["name"]['last name'],
                                                            data['course']['course name'],data['joinedOn']['dd'],data['joinedOn']['mm'],data['joinedOn']['yy'],
                                                            data['completedOn']['dd'],data['completedOn']['mm'],data['completedOn']['yy'],data['course']['duration']))
    
    
            

'''
COLLECT INFORMATION ABOUT A CONTACT: 
fullname, phoneNumber, Birthday-Month & Day

DISPLAY THE COLLECTED CONTACTS IN THE SORTED ORDER OF BIRTHDAY
IF 2 CONTACTS HAVE THE SAME BIRTHDAY, ORDER THEM IN THE ASCENDING ORDER OF PHONE NUMBER


'''
details_of_user_list=[]         #Empty list to append user details
months={1:(31,'Jan'), 2:(28,'Feb'), 3:(31,'Mar'), 4:(30,'Apr'), 5:(31,'May'), 6:(30,'Jun'),
        7:(31,'Jul'), 8:(31,'Aug'), 9:(30,'Sep'), 10:(31,'Oct'), 11:(30,'Nov'), 12:(31,'Dec'),}     #Months name in a dictionary
while 1:
    details_dict = {"id":'',"name": {"First Name":'',"Last Name":'', "Initial":''},"phone number":'',"DOB":{"dd":'','mm':''}}   #New dictionary
    while 1:                                    #checks n == 0 to take teh user name details 
        print("#"*30)
        print("\t", "Creating user details in dictionary")
        first_name=input('Enter your First name > ') or "FirstName"
        last_name=input('Enter your Last name > ') or "LastName"                               #Asks the user to enter first,last & initial or takes default values
        initial=input('Enter your Initial in one letter max(2 letters)  > ') or "X"
        if first_name.isalpha() and last_name.isalpha() and len(initial) <= 2 and initial.isalpha():          #using isalpha() to check name is alphabatic or not if name of user is valid it is stored in dictionary
            details_dict['name']["First Name"]= first_name.title()
            details_dict["name"]['Last Name'] = last_name.title()
            details_dict['name']['Initial']= initial.title()
            break
        else:
            print("*"*30)
            print("Invalid entry Re - Enter the details")
    while 1:
        print("~"*30)                                   
        phone_number = input('Enter phone number >') or "00000000000"               #Takes phone number input from the user
        if len(phone_number) == 10 and phone_number.isnumeric():
            details_dict["phone number"]=phone_number                       #checks the number is numeric and it has 10 characters and if it is true store data
            break
        else:
            print("*"*30)                                           #raises error if phone number not equal to 10 or not numeric
            print("Invalid entry Enter again!")
            
    print("~"*30)
    while 1:
        month=input('''Enter Month
    Enter here: ''')                                            #takes month input from user and checks it is numeric or not
        if month.isnumeric():
            month=int(month)
            if month > 0 and month <=12:                    #if month is numeric checks the number is in between 1 and 12
                break
            else:
                print("Invalid Entry enter again!")             #if user enters invalid entry raise errrou
        else:
            print("Invalid Entry enter again!")                 #if user enters invalid entry raise errrou
    while 1:
        day=input('''Enter Day you born
        Enter here: ''')                                     
        if day.isnumeric():                                 #checks entered day is numeric or not
            day = int(day)
            if day > 0 and day<= months[month][0]:      #check day is matching with number of days in month using month dictionary
                break
            else:
                print("Invalid Entry enter again!")             #if user enters invalid entry raise error
        else:
            print("Invalid Entry enter again!")                 #if user enters invalid entry raise error
    details_dict["DOB"]['dd']=day
    details_dict['DOB']['mm']=month
    details_dict['id']=len(details_of_user_list)+1
    details_of_user_list.append(details_dict)               #store date details in dictionary and appended in list
    del details_dict                                        #deleting dictinary for every loop to avoid overwriting of previous data
    if len(details_of_user_list) >=1:                           #checks the number of user match to atleast 3 or more
        if input("Do you want quit ? y or n or just press enter > ") in 'yY':           #if user are atleast 3 asks user to continue or quit and breaks loop
            break

new_l =[]                                                   #created an empty list to place month,phone number tuples
for i in details_of_user_list:
    data=i
    new_l.append((data['DOB']['mm'],data['phone number']))          #creating a tupple with month, phone number from the details_of_user_list 
new_l.sort()                                                        #sorting the list which has month, phone number tuples
sorted_list=[]                                                      #created empty list to append index of details_of_user_list when the each dict is match with month,phone number tuple
for i in new_l:                                             #for loop for tuple month,phone number list
    for n in range(len(details_of_user_list)):              #for loop with range of length of details_of_user_list to get index
        data=details_of_user_list[n]
        if data['DOB']['mm']== i[0] and int(data['phone number']) == int(i[1]):         #checks for each tuple data equal to each data in details_of_user_list
            sorted_list.append(n)                           #after successfully passing conditon index of details_of_user_list is appended in sorted_list list
for i in sorted_list:
    data=details_of_user_list[i]
    print("ID {}. NAME: {} {} {} DOB: {}/{} Phn: {}".format(data['id'],data['name']['Initial'],data['name']['First Name'],data['name']['Last Name'],
                                                    data['DOB']['dd'],data['DOB']['mm'],data['phone number']))                          #printing the details_of_user_list each data according to sorted_list index

'''
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
'''



details_of_user_list=[]         #Empty list to append user details
months={1:(31,'Jan'), 2:(28,'Feb'), 3:(31,'Mar'), 4:(30,'Apr'), 5:(31,'May'), 6:(30,'Jun'),
        7:(31,'Jul'), 8:(31,'Aug'), 9:(30,'Sep'), 10:(31,'Oct'), 11:(30,'Nov'), 12:(31,'Dec'),}     #Months name in a dictionary
while 1:
    details_dict = {'id':'',"name": {"First Name":'',"Last Name":'', "Initial":''},"phone number":'',"DOB":{"dd":'','mm':'','yy':''}}   #New dictionary
    while 1:                                    #checks n == 0 to take teh user name details 
        print("#"*30)
        print("\t", "Creating user details in dictionary")
        first_name=input('Enter your First name > ') or "FirstName"
        last_name=input('Enter your Last name > ') or "LastName"                               #Asks the user to enter first,last & initial or takes default values
        initial=input('Enter your Initial in one letter max(2 letters)  > ') or "X"
        if first_name.isalpha() and last_name.isalpha() and len(initial) <= 2:          #using isalpha() to check name is alphabatic or not if name of user is valid it is stored in dictionary
            details_dict['name']["First Name"]= first_name
            details_dict["name"]['Last Name'] = last_name
            details_dict['name']['Initial']= initial
            break
        else:
            print("*"*30)
            print("Invalid entry Re - Enter the details")
    while 1:
        print("~"*30)                                   
        phone_number = input('Enter phone number >') or "0000000000"               #Takes phone number input from the user
        if len(phone_number) == 10 and phone_number.isnumeric():
            details_dict["phone number"]=phone_number                       #checks the number is numeric and it has 10 characters and if it is true store data
            break
        else:
            print("*"*30)                                           #raises error if phone number not equal to 10 or not numeric
            print("Invalid entry Enter again!")
            
        print("~"*30)
    while 1:
        year=input('''Enter Year between 1946 and 2006
    Enter here: ''')                                        #takes year input from user and checks it is numeric or not
        if year.isnumeric():
            year = int(year)
            if year >= 1946 and year <=2006:                #if it is numeric check the year between 1946 to 2006
                break
            else:
                print("Invalid Entry enter again!")             #if user enters invalid entry raise errrou
        else:
            print("Invalid Entry enter again!")             #if user enters invalid entry raise error
    while 1:
        month=input('''Enter Month
    Enter here: ''')                                            #takes month input from user and checks it is numeric or not
        if month.isnumeric():
            month=int(month)
            if month > 1 and month <=12:                    #if month is numeric checks the number is in between 1 and 12
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
    details_dict["DOB"]['dd']=day                               #day, month, year is stored in dictionary and appended in user list 
    details_dict['DOB']['mm']=month
    details_dict['DOB']['yy']=year
    details_dict['id']= len(details_of_user_list)+1             #id is created based on length of the user details storing list
    details_of_user_list.append(details_dict)               #store date details in dictionary and appended in list
    del details_dict                                        #deleting dictinary for every loop to avoid overwriting of previous data
    if len(details_of_user_list) >=1:                           #checks the number of user match to atleast 3 or more
        if input("Do you want quit ? y or n or just press enter > ") in 'yY':           #if user are atleast 3 asks user to continue or quit and breaks loop
            break

for i in details_of_user_list:          #After completion of loop it print each data in a list
    data=i
    print("ID.{} NAME: {} {} {}  PHN: {} DOB: {}/{}/{}".format(data['id'],data['name']['Initial'],data['name']['First Name'],data['name']['Last Name'],data['phone number'],data['DOB']['dd'],data['DOB']['mm'],data['DOB']['yy']))

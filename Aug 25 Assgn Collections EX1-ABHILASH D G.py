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



details_of_user_list=[]        
months={1:(31,'Jan'), 2:(28,'Feb'), 3:(31,'Mar'), 4:(30,'Apr'), 5:(31,'May'), 6:(30,'Jun'),
        7:(31,'Jul'), 8:(31,'Aug'), 9:(30,'Sep'), 10:(31,'Oct'), 11:(30,'Nov'), 12:(31,'Dec'),}    
while 1:
    details_dict = {'id':'',"name": {"First Name":'',"Last Name":'', "Initial":''},"phone number":'',"DOB":{"dd":'','mm':'','yy':''}}  
    while 1:                                   
        print("#"*30)
        print("\t", "Creating user details in dictionary")
        first_name=input('Enter your First name > ') or "FirstName"
        last_name=input('Enter your Last name > ') or "LastName"                              
        initial=input('Enter your Initial in one letter max(2 letters)  > ') or "X"
        if first_name.isalpha() and last_name.isalpha() and len(initial) <= 2:      
            details_dict['name']["First Name"]= first_name
            details_dict["name"]['Last Name'] = last_name
            details_dict['name']['Initial']= initial
            break
        else:
            print("*"*30)
            print("Invalid entry Re - Enter the details")
    while 1:
        print("~"*30)                                   
        phone_number = input('Enter phone number >') or "0000000000"              
        if len(phone_number) == 10 and phone_number.isnumeric():
            details_dict["phone number"]=phone_number                      
            break
        else:
            print("*"*30)                                          
            print("Invalid entry Enter again!")
            
        print("~"*30)
    while 1:
        year=input('''Enter Year between 1946 and 2006
    Enter here: ''')                                      
        if year.isnumeric():
            year = int(year)
            if year >= 1946 and year <=2006:          
                break
            else:
                print("Invalid Entry enter again!")             
        else:
            print("Invalid Entry enter again!")             
    while 1:
        month=input('''Enter Month
    Enter here: ''')                                            
        if month.isnumeric():
            month=int(month)
            if month > 1 and month <=12:                   
                break
            else:
                print("Invalid Entry enter again!")            
        else:
            print("Invalid Entry enter again!")                 
    while 1:
        day=input('''Enter Day you born
        Enter here: ''')                                     
        if day.isnumeric():                                 
            day = int(day)
            if day > 0 and day<= months[month][0]:    
                break
            else:
                print("Invalid Entry enter again!")             
        else:
            print("Invalid Entry enter again!")                
    details_dict["DOB"]['dd']=day
    details_dict['DOB']['mm']=month
    details_dict['DOB']['yy']=year
    details_dict['id']= len(details_of_user_list)+1            
    details_of_user_list.append(details_dict)               
    del details_dict                                        
    if len(details_of_user_list) >=1:                          
        if input("Do you want quit ? y or n or just press enter > ") in 'yY':           
            break

for i in details_of_user_list:         
    data=i
    print("ID.{} NAME: {} {} {}  PHN: {} DOB: {}/{}/{}".format(data['id'],data['name']['Initial'],data['name']['First Name'],data['name']['Last Name'],data['phone number'],data['DOB']['dd'],data['DOB']['mm'],data['DOB']['yy']))

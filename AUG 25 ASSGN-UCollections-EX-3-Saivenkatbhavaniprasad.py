'''
collects valid day, month,year from the user and print the next day from current day
'''
months={1:(31,'Jan'), 2:(28,'Feb'), 3:(31,'Mar'), 4:(30,'Apr'), 5:(31,'May'), 6:(30,'Jun'),
        7:(31,'Jul'), 8:(31,'Aug'), 9:(30,'Sep'), 10:(31,'Oct'), 11:(30,'Nov'), 12:(31,'Dec'),}     #months places in dictionary
date_dict = {"date":{'dd':'',"mm":'',"yy":''},'next day':{'dd':'','mm':'',"yy":''}}
print("~"*30)
print('\t','\t','Date details collecting')
while 1:
    year = input("Enter year > ")                           #takes year input from the user
    if year.isnumeric():                                    #checks input in numeric form
        year = int(year)
        break
    else:
        print("*"*30)
        print('\t','\t',"Invalid input enter again !")      #if user not enter input in numeric form raise error
date_dict['date']['yy']=year                                #stores year in yy in date_dict
while 1:
    month = input("Enter month > ")                         #takes month input from user
    if month.isnumeric():                                   #checks entered month is numeric or not
        month = int(month)
        if month>0 and month <=12:                          #check month is between 1 and 12 or else raise error
            break
        else:
            print("*"*30)
            print('\t','\t',"Invalid input enter again !")
    else:
        print("*"*30)
        print('\t','\t',"Invalid input enter again !")      #if input is not numeric raise error
date_dict['date']['mm']=month                               #month is stored in mm in date_dict
while 1:
    leap_or_no =0
    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):        #checks entered year is leap year or not
        leap_or_no =1                                       #if leap year leap_or_no is update to 1
    day = input("Enter day > ")                             #takes day input from user
    if day.isnumeric():                         
        day = int(day)
        if leap_or_no==1: 
            if month == 2:                                  #if year is leap year  and month is 2 check day is between 1 and 29 
                if day >0 and day <=29:
                    break                                   #after passing conditons breaks the loop
                else:
                    print("*"*30)
                    print('\t','\t',"Invalid input enter again !") #if day is not between 1 and 29 raise error
            else:
                if day > 0 and day <= months[month][0]:     #if year is not leap year  and month is 2 check day is between 1 and 28
                    break
                else:
                    print("*"*30)
                    print('\t','\t',"Invalid input enter again !")        #if day is not correct raise error
        else:
            if day > 0 and day <= months[month][0]:         #checks remaining months except feb, entered day is between 1 and 31 or 31 according to month
                break                                       #after successful entry breaks the loop
            else:
                print("*"*30)
                print('\t','\t',"Invalid input enter again !")        #if day is not correct raise error
    else:
        print("*"*30)
        print('\t','\t',"Invalid input enter again !")                #if input is not numeric rasie error
date_dict['date']['dd']=day                                 #day is stored in dd in date_dict
next_day =day
next_month =month                                           #taken day,month,year as default values to next_day,next_month,next_year
next_year = year
if month == 2:                                              #checks month is 2 
    if day == 29 or day == 28:                              #if yes checks day is 28 or 29
        next_day =1
        next_month =3                                       #if entered day is end of the month it updates the day and month to next month
    else:
        next_day = next_day+1                               #for remaining days in feb the day is updated to next day
elif month in [1,3,5,7,8,10,12]:                            #checks month in months with 31 days
    if month == 12 :                                        #checks the month is december 
        if day== 31:                                        #if day is 31 which is end of month and if it is december
            next_day = 1
            next_month =1                                   #day updated,month is updated to next month, year is updated to new year
            next_year = next_year+1
        else:
            next_day = next_day+1                           #remaining day in december is update to next day
    else:
        if day == 31:                                       #if months are not december and day is 31
            next_day = 1
            next_month = month+1                            #day is updated  and month is updated to next month
        else:
            next_day =day+1                                 #if day is not 31 the day is updated to next day
elif month in [4,6,9,11]:                                   #checks month with months with 30 days
    if day == 30:                                           #checks day is 31
        next_day = 1                                        #if day is 31 day is updated and month is updated to next month
        next_month = month+1
    else:
        next_day =next_day+1                                #if day is not 31 the day is updated to next day
date_dict['next day']['dd']= next_day
date_dict['next day']['mm']=next_month                      #next_day, next_month, next_year is stored in dd, mm ,yy in next day in date_dict
date_dict['next day']['yy']= next_year
print("\t",'\t',"~"*10,'Output of the enterd date',"~"*10)
#print the output in clean way using .format() and data is taken from the date_dict
print('\t','\t',"Next day to {}/{}/{} is {}/{}/{}".format(date_dict['date']['dd'],date_dict['date']['mm'],date_dict['date']['yy'],date_dict['next day']['dd'],date_dict['next day']['mm'],date_dict['next day']['yy']))

        

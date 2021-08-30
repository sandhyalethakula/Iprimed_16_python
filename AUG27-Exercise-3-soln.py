'''          Next Day ( immediate successor)
        ```````````````````````````````````````````````
Write a program that reads a date from the user and computes its immediate successor.

For example, if the user enters values that represent 2013-11-18
    then your program should display a message indicating that the day
    immediately after 2013-11-18 is 2013-11-19.

If the user enters values that represent 2013-11-30
    then the program should indicate that the next day is 2013-12-01.

If the user enters values that represent 2013-12-31
    then the program should indicate that the next day is 2014-01-01.
------------------------------------------

The date will be entered in numeric form with three separate input statements;
one for the year,
one for the month,
and one for the day.

1. Ensure that your program works correctly for leap years.
2. Validate the entries
3. Print the entered date & the computed next day in the format: dd/monthName/yyyy
'''

# Month data to validate & print
months={1:(31,'Jan'), 2:[28,'Feb'], 3:(31,'Mar'), 4:(30,'Apr'), 5:(31,'May'), 6:(30,'Jun'),
        7:(31,'Jul'), 8:(31,'Aug'), 9:(30,'Sep'), 10:(31,'Oct'), 11:(30,'Nov'), 12:(31,'Dec'),}

enteredDate=''
calcDate=''

while 1:
    while 1:
        yy=input('Enter valid year as a number. > ')  or '2021'
        #validate
        if len(yy)==4:
            if yy.isnumeric():
                yy=int(yy)
                # leap year
                if((yy % 400 == 0) or (yy % 100 != 0) and (yy % 4 == 0)):
                    months[2][0]=29
                else:
                    months[2][0]=28                          
                break
            
    while 1:
        mm=input('Enter valid month as a number. > ')  or '7'
        #validate
        if mm.isnumeric():
            mm=int(mm)
            if mm >=1 and mm<=12:
                break        
    
    while 1:        
        dd=input('Enter valid day as number: > ') or '12'
        #validate
        if dd.isnumeric():
            dd=int(dd)
            if dd>=1 and dd<=months[mm][0]:
                break

    enteredDate='/'.join([str(dd),months[mm][1],str(yy)])
    
    # NEXT DAY:-----------calculate next date -------------------------------
    nxd_d = nxd_m = nxd_y = 0
    if dd == months[mm][0]:
        nxd_d = 1
        if mm == 12:
            nxd_m = 1
            nxd_y = yy + 1
        else:
            nxd_m = mm + 1
            nxd_y = yy
    else:
        nxd_d = dd+1
        nxd_m = mm
        nxd_y = yy

    calcDate='/'.join([str(nxd_d),months[nxd_m][1],str(nxd_y)])
    #----------------------------------------------------    
    print('Entered:', enteredDate, 'NextDay:', calcDate)
# end the data collection loop
    if input('Do you want to quit? > y/n or just press enter >') in 'yY':break
        
#````````````````````````````````````````````````````````````````````



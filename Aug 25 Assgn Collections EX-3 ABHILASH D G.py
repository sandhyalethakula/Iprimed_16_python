"""'''          Next Day ( immediate successor)
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
"""

months={1:(31,'Jan'), 2:(28,'Feb'), 3:(31,'Mar'), 4:(30,'Apr'), 5:(31,'May'), 6:(30,'Jun'),
        7:(31,'Jul'), 8:(31,'Aug'), 9:(30,'Sep'), 10:(31,'Oct'), 11:(30,'Nov'), 12:(31,'Dec'),}
while 1:
        yy=input('enter a year>') 
        if yy.isnumeric():
            yy=int(yy)
            break
            
#taking minth from user and validating
while 1:
     mm=input('enter valid month as a number > ') 
     if mm.isnumeric():
         
        mm=int(mm)
        if mm>=1 and mm<=12:break
#taking day and validating
while 1:
    dd=input('enter valid day as number>')
    if dd.isnumeric():
        dd=int(dd)
        if dd>=1 and dd <=months[mm][0]:break

if yy%400==0 or (yy%4==0 and yy%100!=0):
    

   #leap year

   if mm==2:

       no_of_days=29

   elif mm in [4,6,9,11]:

       no_of_days=30

   else:

       no_of_days=31

else:

   #not a leap year

   if mm==2:

       no_of_days=28

   elif mm in [4,6,9,11]:

       no_of_days=30

   else:

       no_of_days=31

if dd<no_of_days:

   print(dd+1,"-",mm,"-",yy)

else:

   if mm==12:

       print(1,"-",1,"-",yy+1)

   else:

       print(1,"-",mm+1,"-",yy)

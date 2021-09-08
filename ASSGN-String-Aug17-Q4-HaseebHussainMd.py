'''
Accept month, emp name and salary from user
if Salary > 600000, add a bonus of 2500
if salary <= 600000, add a bonus of 6000
print a salary slip
'''
m=input('enter the month :')
name=input('enter the emp name : ')
s=int(input('enter salary : '))
if s>600000 :   
    total=s+2500
    b=str(2500)
elif s<=600000:
    total=s+6000
    b=str(6000)

print('-'*29);print('name    :',name);print('salary  :',s);print("bonus   :",b);print('total   :',total);print('-'*29)
    

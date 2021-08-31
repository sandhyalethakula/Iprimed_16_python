"""EX-1
Accept month, emp name and salary from user
if Salary > 600000, add a bonus of 2500
if salary <= 600000, add a bonus of 6000
print a salary slip
--------------------------
    name : ____
    sal  : ____
    bonus: ____
    total: ____
--------------------------"""


mnth=input("enter month:")
name=input("enter name:")
sal=int(input("enter salary:"))
if sal>60000:
    sal=sal+2500
    bo=2500
else:
    sal=sal+6000
    bo=6000
print("-"*50)
print("\t\tName:",name,"\n\t\tSalary:",sal,"\n\t\tBonus:",bo)
print("-"*50)

           

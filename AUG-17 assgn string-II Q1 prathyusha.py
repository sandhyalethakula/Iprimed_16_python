''' EX-1
Accept month, emp name and salary from user
if Salary > 600000, add a bonus of 2500
if salary <= 600000, add a bonus of 6000
print a salary slip
--------------------------
    name : ____
    sal  : ____
    bonus: ____
    total: ____
--------------------------
'''

employee_name = input("Enter your name >")
month=input("enter month >")
salary =int(input("Enter your salary >"))

print("-"*50)
if salary > 600000:
   
    print("name:- "+ employee_name,"month:-"+month, "Employee salary:- "+ str(salary), "Bonus:- "+ "2500", "Total salary:- "+ str(salary+2500),sep="\n")
else:
    print("name:- "+ employee_name,"month:-"+month, "Employee salary:- "+ str(salary), "Bonus:- "+ "6000", "Total salary:- "+ str(salary+6000),sep="\n")
    print("-"*50)

'''
EX-1
Accept month, emp name and salary from user
if Salary > 600000, add a bonus of 2500
if salary <= 600000, add a bonus of 6000
print a salary slip
--------------------------
    name : ________
    sal  : ________
    bonus: ________
    total: ________
--------------------------
'''

employee_name = input("Enter your name >")          #asks user to enter name 
salary =int(input("Enter your salary >"))           #asks emp salary from user

if salary > 600000:                                 #if salary is greater than 600000, 2500 is added as bonus
    print("name:- "+ employee_name, "Employee salary:- "+ str(salary), "Bonus:- "+ "2500", "Total salary:- "+ str(salary+2500),sep="\n")
else:
    print("name:- "+ employee_name, "Employee salary:- "+ str(salary), "Bonus:- "+ "6000", "Total salary:- "+ str(salary+6000),sep="\n")
                                                    #if salary is less than 600000, 6000 is added as bonus

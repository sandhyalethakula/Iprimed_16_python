'''3.	Question
Generate the pattern: 
	5555555555 
	44444444 
	333333 
	2222 
	11
	
'''
num = int(input("Enter a number >"))#read input from the user

while num > 0:#num is greater than 0
    print(str(num) * num*2)
    num-=1

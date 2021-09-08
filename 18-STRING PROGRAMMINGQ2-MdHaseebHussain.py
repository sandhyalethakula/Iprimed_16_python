'''
2. Write a program that asks the user to enter two strings of the same length. The program should then check to see if 
the strings are of the same length. If they are not, the program should print an appropriate message and exit. If they 
are of the same length, the program should alternate the characters of the two strings. 
For example, if the user enters abcde and ABCDE the program should print out:
AaBbCcDdEe
'''
x1=input('enter the first string : ')
x2=input('enter the second string : ')
d=0
if len(x1) != len(x2) :
    print('you entered wrong inputs ')
else:
    while d < len(x1):
        print(x1[d]+x2[d],end='')
        d+=1

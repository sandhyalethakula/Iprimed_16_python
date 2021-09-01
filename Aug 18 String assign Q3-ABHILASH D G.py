"""Write a program that asks the user to enter two strings of the same length. The program should then check to see if
the strings are of the same length. If they are not, the program should print an appropriate message and exit. If they
are of the same length, the program should alternate the characters of the two strings.
For example, if the user enters abcde and ABCDE the program should print out:
AaBbCcDdEe
"""


#mix string 1 and 2
name1=input("enter the frst string")
name2=input("enter the second string")
a=len(name1)
b=len(name2)
if a!=b:   #if both the strings are not same next statement will print
    print("Two input are not same")
else:
    res=""
    for i in range(a):         #if strings are same then it will join
        res+=name1[i]
        res+=name2[i]
    print(res)

    print('--'*35)

'''
1. Write a program that asks the user to enter a word that contains the letter a. The program should then print the 
following two lines: On the first line should be the part of the string up to and including the first a, and on the 
second line should be the rest of the string. 
Sample output is shown below: 
>>> Enter a word: buffalo 
buffa
lo
'''
S1=input("Enter the String >")
m=len(S1)
for i in range(m):      #checking line by line
    if S1[i]=="a":      #if string contain a it split the string
        print(S1[:i+1],S1[i+1:],sep="\n")
        break

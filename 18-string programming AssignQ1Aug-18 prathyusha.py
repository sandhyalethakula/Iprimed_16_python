'''Write a program that asks the user to enter a word that contains the letter a. The program should then print the 
following two lines: On the first line should be the part of the string up to and including the first a, and on the 
second line should be the rest of the string. 
Sample output is shown below: 
>>> Enter a word: buffalo 
buffa 
lo
'''



'''
input_word = input("Enter a word >")                                #takes input from the user
for i in range(len(input_word)):
    if input_word[i]=="a":                                              #iterates each word and checks the first a and using the a index print output
        print(input_word[:i+1],input_word[i+1:],sep="\n")
        break
'''



s1=input("enter the string:")
s2=s1.split("a")
print(s2[0]+"a")
print(s2[1])

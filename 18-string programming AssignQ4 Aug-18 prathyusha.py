'''
Write a program that asks the user to enter their full name in lowercase and then capitalizes the first letter of each word of their name and print it.
'''

full_name = input("Enter full name in lower case >")    #takes input from user

full_name = full_name.split()
for i in full_name:                     
    print(i[0].upper()+i[1:], end=" ")                      #convert the first letter of word into capital







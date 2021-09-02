'''
 2.Write a program that asks the user to enter a word and then capitalizes every other letter of that word. So if the 
user enters rhinoceros, the program should print rHiNoCeRoS.
'''

user_input= input("Enter a word >")                     #takes input from user
word = ''
d=0
while d < len(user_input):                              #iterate each value from the input
    if d%2 == 1:
        word+=user_input[d].upper()                     #check for odd index and converting them into uppercase words
    else:
        word+=user_input[d]                             #for even index it will remains same
    d+=1                                                #d is increased by +1 to break loop and also change the index nuber
print(word)                                             #prints the final output

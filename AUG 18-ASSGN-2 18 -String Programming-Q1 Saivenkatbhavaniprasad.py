'''
. Write a program that asks the user to enter a word that contains the letter a. The program should then print the 
following two lines: On the first line should be the part of the string up to and including the first a, and on the 
second line should be the rest of the string. 
Sample output is shown below: 
>>> Enter a word: buffalo 
buffa 
lo
'''

input_word = input("Enter a word >")                                    #takes input from the user
d=0
while d < len(input_word):
    if input_word[d]=="a":                                              #iterates each word and checks the first a and using the a index print output
        print(input_word[:d+1],input_word[d+1:],sep="\n")               #if letter is i breaks loop and divide the word using string slicing method
        break
    d+=1                                                                #d is increased by +1 to break the loop and it also indicates the index of each letter in a word

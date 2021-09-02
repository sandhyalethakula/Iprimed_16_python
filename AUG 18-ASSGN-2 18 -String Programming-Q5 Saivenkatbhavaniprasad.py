'''
Write a program that generates the 26-line block of letters partially shown below.
abcdefghijklmnopqrstuvwxyz 
bcdefghijklmnopqrstuvwxyza 
cdefghijklmnopqrstuvwxyzab 
... 
yzabcdefghijklmnopqrstuvwx 
zabcdefghijklmnopqrstuvwxy 
abcdefghijklmnopqrstuvwxyz
'''

input_words = "abcdefghijklmnopqrstuvwxyz"      #input words from a to z
d=0                                             #default index value 0
while d <= len(input_words):                    #iterates each word from the input_word
    first = input_words[d:]                     #first is from d to end of the string
    second = input_words[:d]                    #second is a from start to d
    print(first+second)                         #prints the output with join of second and first to get output as required ex: bcdefghijklmnopqrstuvwxyza 
    d+=1                                        #d value is increased by +1 for each loop to break the loop and also changes the index value to iterate letters
                                

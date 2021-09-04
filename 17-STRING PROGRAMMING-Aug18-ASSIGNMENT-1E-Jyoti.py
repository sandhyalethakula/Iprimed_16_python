'''
5. Write a program that asks the user to enter a string, then prints out each letter of the string doubled and on a 
separate line. 
For instance, if the user entered HEY, the output would be:
HH 
EE 
YY
'''

word = input('Enter a word > ')                 #user will enter a word

for i in word:                                  #prints the each word with multiple of 2
    print(i*2)

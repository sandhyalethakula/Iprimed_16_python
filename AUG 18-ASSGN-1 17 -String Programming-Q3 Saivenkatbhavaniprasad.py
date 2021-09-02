'''
3. Write a program that asks the user to enter a string s (multiple sentences) and then converts s to lowercase, 
removes all the periods and commas from s, and prints the resulting string. 
'''

word = input('Enter a word > ')         #asks user to enter a word
result=''                               #empty string to add letters
for i in word:
    if i.isalpha():                     #checks each letter is alpha or not using isalpha()
        result+=i.lower()               #if letter is alpha the it is converted into lower and added to result
    elif i == ' ':
        result+=i                       #if there is space between two names the it will also added
print(result)                           #prints the final output with lowercase letters

'''
4. Write a program that asks the user to enter a word and determines whether the word is a palindrome or not. A 
palindrome is a word that reads the same backwards as forwards.
'''
word = input('Enter a word > ')             #asks user to enter a word

if word == word[::-1]:                      #checks the input word with reverse of input word to find it is palindrome or not       
    print(word,'is a palindrome')           #if it is palindrome then it prints input is a palindrome
else:
    print(word,'is not a palindrome')       #if it is not palindrome then it prints input is not a palindrome

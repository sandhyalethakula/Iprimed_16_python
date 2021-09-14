'''
4.Write a program that asks the user to enter a word and determines whether the word is a palindrome or not. A 
palindrome is a word that reads the same backwards as forwards
'''
str=input(("Enter a string:"))
if(str==str[::-1]):     #slice operation, -1 reverses the string
      print("The string is a palindrome")
else:
      print("Not a palindrome")
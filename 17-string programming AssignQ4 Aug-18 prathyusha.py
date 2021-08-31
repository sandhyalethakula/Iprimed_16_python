'''write a program that asks the user to enter a word and determines whether the word is a polindrome or not. A palindrome is a word that reads the same backwards as forwards'''

n=input("enter a word:")                           #takes input from user
if n==n[::-1]:
	print("it is palindrome")                                #palindrome
else:
	print("not a palindrome")                              #not palindrome
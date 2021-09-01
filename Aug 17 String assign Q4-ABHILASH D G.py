

  
"""write a program that asks the user to enter a word and determines whether the word is a polindrome or not. A palindrome is a word that reads the same backwards as forwards
"""
string=input(("Enter a letter:"))  
if(string==string[::-1]):  
      print("The letter is a palindrome")  
else:  
      print("The letter is not a palindrome")  

"""Write a program that asks the user to enter their full name in lowercase and then capitalizes the first letter of each
word of their name and print it."""

s = 'hello welcome to india'
s = ' '.join(word[0].upper() + word[1:] for word in s.split())  #first splitting the words and joining is done
print(s)

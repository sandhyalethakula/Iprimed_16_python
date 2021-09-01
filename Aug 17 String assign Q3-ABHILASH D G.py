'''write a program that asks the user to enter a string s (multiple sentences) and then converts s to lowercase, removes all the periods and commas from s, and prints the resulting string.'''


str=input("enter a string:")
word=''
for i in str:
	if i.isalpha():
		word+=i.lower()             
	else:
		word+=""
print(word)

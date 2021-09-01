'''write a program that asks the user to enter a string s (multiple sentences) and then converts s to lowercase, removes all the periods and commas from s, and prints the resulting string.'''


str=input("enter a string:")
word=''
for i in str:
	if i.isalpha():
		word+=i.lower()             #print each word in lower case
	else:
		word+=""
print(word)





'''
string=input("Enter a string> ")
punctuation=',','.'
for x in string.lower():
    if x in punctuation:
        string=string.replace(x,"")
        print(string.lower())
'''

'''write a program that asks the user to enter a word and prints out whether that word containsvowels and if so, how many'''



while 1:
	vcount=0
	str=input("enter a string:")                   #takes input from user
	str=str.lower()                                 #coverts string to lowercase
	for i in range(0,len(str)):
		if str[i] in ("a","e","i","o","u"):             #checks if vowels are present
			vcount=vcount+1                             
	print("total number of vowel :")                       #prints the total no.of vowels
	print(vcount)
	break

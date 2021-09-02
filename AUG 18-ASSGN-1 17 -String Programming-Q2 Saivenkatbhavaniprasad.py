'''
Write a program that asks the user to enter a word and prints out whether that word contains any vowels and if so, 
how many
'''

word = input("Enter a word >")              #Takes string as input
count = 0
for i in word:                                  
    if i in "aeiou":                        #checks each letter is vowel or not if vowel count increased to +1
        count+=1
print("The number of vowels present in the word is",count)          #prints number of vowels and their count


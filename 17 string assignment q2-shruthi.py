'''Ask the user for a input and print the number of vowels in it and check how many are there'''





n= input ("enter a word: ")

v = 0
for i in n:
    if i in 'aeiou':
        v=v+1
        print("Vowel(s) present in the word")
        print(v)
    else:
        print (" no vowel found")
    

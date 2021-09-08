'''
Write a program that asks user to enter a word and prints out whether the word contains any vowels if so, how many?
'''



str=input('enter a string')
vowels = 0
for i in str:
    if i in 'aeiou':
        vowels = vowels+1
print('no.of vowels are: ')
print(vowels)

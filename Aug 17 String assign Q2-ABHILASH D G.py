'''write a program that asks the user to enter a word and prints out whether that word containsvowels and if so, how many'''


str=input("enter string")
count=0
for c in str :
    if c in ['a', 'e', 'i', 'o', 'u']:
        count += 1
print(count)

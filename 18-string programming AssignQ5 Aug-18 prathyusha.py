'''Write a program that generates the 26-line block of letters partially shown below.
abcdefghijklmnopqrstuvwxyz 
bcdefghijklmnopqrstuvwxyza 
cdefghijklmnopqrstuvwxyzab 
... 
yzabcdefghijklmnopqrstuvwx 
zabcdefghijklmnopqrstuvwxy 
abcdefghijklmnopqrstuvwxyz
'''
'''
input_words = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(input_words)+1):         #iterates each word from the input_word
    first = input_words[i:]
    second = input_words[:i]                #prints the output
    print(first+second)

'''



letters='abcdefghijklmnopqrstuvwxyz'

ctr=0
while ctr<len(letters):
    print(letters[ctr:]+letters[:ctr])
    ctr+=1

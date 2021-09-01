'''Write a program that generates the 26-line block of letters partially shown below.
abcdefghijklmnopqrstuvwxyz 
bcdefghijklmnopqrstuvwxyza 
cdefghijklmnopqrstuvwxyzab 
... 
yzabcdefghijklmnopqrstuvwx 
zabcdefghijklmnopqrstuvwxy 
abcdefghijklmnopqrstuvwxyz
'''



letters='abcdefghijklmnopqrstuvwxyz'

ctr=0
while ctr<len(letters):
    print(letters[ctr:]+letters[:ctr])
    ctr+=1

'''
4.Write a program that generates the 26-line block of letters partially shown below.
abcdefghijklmnopqrstuvwxyz 
bcdefghijklmnopqrstuvwxyza 
cdefghijklmnopqrstuvwxyzab 
... 
yzabcdefghijklmnopqrstuvwx 
zabcdefghijklmnopqrstuvwxy 
abcdefghijklmnopqrstuvwxyz
'''

s='abcdefghijklmnopqrstuvwxyz'
c=0
while c<len(s):
    print(s[c:] + s[:c:1])
    c=c+1

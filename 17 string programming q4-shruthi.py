'''check if palindrome'''

n=input("enter a word: ")
if n == n[::-1]:
    print('its a palindrome')
else:
    print("not a palindrome")

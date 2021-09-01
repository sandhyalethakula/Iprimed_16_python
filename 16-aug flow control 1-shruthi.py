"""1.Accept a number between 5 and 30
a.if the number is less than 10 , multiply by 5 and print the result
b.if the number is > 25 , subtract 5 and print the result
c.if the number is >=10 and <=15 ,add 5 and print the result
d.if the number is >20,divide by 5 and print the result
e.if the number does not satisfy these condition,print the number """


n=int(input("Enter a number only between 5 and 30:"))
if n >= 5 and n <10:
    a=n*5
    print(a)
elif n >= 25 and n < 30:
    a=n-5
    print(a)
elif n >= 10 and n <=15:
    a=n+5
    print(a)
elif n >= 20 and n < 25:
    a=n/5
    print(a)
else:
    print(n)

"""Accept a number between5 and 30 from the user
 a.If the number is less than 10,multipy by 5 and print the result
 b.If the number is >25, subtract 5 and print the result
 c.If the number is >10 and <=15, add 5 and print the result
 d.If the number is >20,divide by 5 and the result.
 e.If the number does not satisfy these conditions print the number"""


n=int(input("Enter a number> "))
if n>=5 and n<=30:
    if n<10:
        print(n*5)
    elif n>25:
        print(n-5)
    elif n>=10 and n<=15:
        print(n+5)
    elif n>20:
        print(n//5)
    else:
        print(n)
else:
     print(n)
        

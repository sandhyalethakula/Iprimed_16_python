#third starting from n=2
c=2
while c<=10:
    print("*"*c)
    c=c+1
"""Number pattern"""
c=5
n=1
while n<c:
    while c>=1:
        print(str(c)*c*2)
        c=c-1
        continue
    n=n+1
    break

"""3.	Question
Generate the pattern: 
	5555555555 
	44444444 
	333333 
	2222 
	11
	0"""
c=5
n=5
while n>=0: #if n is greater than zero then it will execute the following statements
    print(str(c)*n*2)
    c=c-1
    n=n-1
    if n==0:
     print(0)
"""Equal numbers of pattern"""
c=1
while c<6:
    print("*"*5)
    c+=1
"""Down pyramid of pattern"""
c=5
while c:
    print("#"*c)
    c-=1

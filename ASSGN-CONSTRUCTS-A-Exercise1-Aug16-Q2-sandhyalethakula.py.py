'''2.	ACCEPT 2 NUMBERS FROM THE USER. 
a.	IF THE 2 NUMBERS ARE EQUAL, PRINT THE APPROPRIATE MESSAGE
b.	IF THE FIRST NUMBER IS GREATER, PRINT THE APPROPRIATE MESSAGE
c.	IF THE SECOND NUMBER IS GREATER, PRINT THE APPROPRIATE MESSAGE
d.	IF THE USER DOES NOT ENTER A NUMBER, PRINT ERROR AND GET THE NUMBERS AGAIN

'''

while 1:
    n=input('Num? or Qq to quit >')
    if n:
        if n in 'Qq':break
        ctr=0
        l=len(n)
        while ctr<1:
            if n[ctr] not in '0123456789-+j.':
                print(n[ctr],'not num');
                break
            if ('-' in n and n[0]!='-'):
                    print('not num');
                    break
                
            ctr+=1
                    
        else:
             print('it is a num!')
             if'.'in n:
                 n=float(n)
             elif 'j' in n:
                 n=complex(n)
                 print('n+2',n+2)
             else:
                 n=int(n)
                 print('n+2=',n+2)
                 break 
    else:
        print('not num')

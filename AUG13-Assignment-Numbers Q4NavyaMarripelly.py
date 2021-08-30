'''
6.ACCEPT A NUMBER FROM THE USER AND PRINT IF IT IS ‘EVEN’ OR ‘ODD’
'''
number = int(input('Enter a number >'))     #Asks user to enter a number to find it is even or not

if number % 2 == 0:                         #if modules of number by 2 equal to 0 then it is even or it is odd
    print(number,"is even number")          #prints if it is even
else:
    print(number,"is odd number")           #if number is not equal to 0 then it is odd and print

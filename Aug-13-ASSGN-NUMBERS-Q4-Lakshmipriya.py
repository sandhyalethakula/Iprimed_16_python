'''4.ACCEPT A NUMBER FROM THE USER AND PRINT IF IT IS ‘EVEN’ OR ‘ODD’'''

print('-'*20)
num = int(input("Enter a number: "))  #Read input from the user 
if (num % 2) == 0:  #check num%2==0 deciding for the even or odd
   print("{0} is Even number".format(num))  
else:  
   print("{0} is Odd number".format(num))
print('-'*20)

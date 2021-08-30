
'''3.Write a program that begins by reading a temperature from the user in degrees Celsius.
Then your program should display the equivalent temperature in degrees Fahrenheit. (fahrenheit = (celsius * 9/5) + 32)'''

print('-'*20)
celsius = float(input('Enter temperature in Celsius: '))  #Read input from the user 
fahrenheit = (celsius * (9/5)) + 32  # calculate temperature in Fahrenheit  
print('%0.1f  Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))
print('-'*20)

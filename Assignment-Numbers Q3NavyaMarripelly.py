'''
5.Write a program that begins by reading a temperature from the user in degrees Celsius. Then your program should display the equivalent temperature in degrees Fahrenheit. (fahrenheit = (celsius * 9/5) + 32)
'''

celsius_temperature = int(input('Enter celsius temperature > '))    #ask user to enter celsius temperature
calculate_fahrenheit = (celsius_temperature * 9/5) + 32             #calculate fahrenheit by using formula
print("Temperature is",int(calculate_fahrenheit),"degree fahrenheit")    #fahrenheit temperature is printed

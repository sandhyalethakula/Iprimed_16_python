'''
5.Write a program that begins by reading a temperature from the user in degrees Celsius. Then your program should display the equivalent temperature in degrees Fahrenheit. (fahrenheit = (celsius * 9/5) + 32)
'''

temperature = int(input('Enter celsius temperature > '))    # enter celsius temperature
fahrenheit = (temperature * 9/5) + 32             #calculate fahrenheit by using formula
print(fahrenheit)

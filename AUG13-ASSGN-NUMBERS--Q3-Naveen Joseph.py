'''3.Write a program that begins by reading a temperature from the user in degrees Celsius.
Then your program should display the equivalent temperature in degrees Fahrenheit.
(fahrenheit = (celsius * 9/5) + 32)'''
n = input("Enter the temperature in celisius : ")
cel = int(n)
m = cel * (9/5)
fahrenheit = m + 32#the fahrenheit is calculated
print("The Fahrenheit equivalent of ",cel," is ",fahrenheit)

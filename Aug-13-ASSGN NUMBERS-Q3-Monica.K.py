# Write a program that begins by reading a temperature from the user in degrees Celsius.
# Then your program should display the equivalent temperature in degrees Fahrenheit.
# (fahrenheit = (celsius * 9/5) + 32)

n=int(input("Enter the temparature in celsius : "))
f=float((n*9/5)+32)
print("The Fahrenheit equivalent of the",n,"degree celsius is",f)

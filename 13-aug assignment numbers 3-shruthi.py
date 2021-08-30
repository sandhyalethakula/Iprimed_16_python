"""3.Write a program that begins by reading a temperature from the user in degrees celsius.Then your program should display the equivalent temperature
in degrees fahrenheit. """


c=float(input("Enter the temperature in degree celcius"))                #getting user input
f=(c*9/5)+32                                                            # formula to convert c to f
print("The temperature in fahrenheit =",f)                               # printing the temperature

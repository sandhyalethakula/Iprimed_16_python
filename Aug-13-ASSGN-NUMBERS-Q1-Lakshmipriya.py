'''1.Write a program that reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n.
The sum of the first n positive integers can be computed using the formula: sum = (n)(n + 1) / 2 '''

print('-'*20)
n = int(input("Enter a positive integer: ")) #Read the input from the user
total = n * (n+1) / 2 #Calculate the sum
print("The sum of the first",n,"positive integers",total)#Display the result
print('-'*20)




'''1.Write a program that reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n.
The sum of the first n positive integers can be computed using the formula: sum = (n)(n + 1) / 2 '''.
#Read the input from the user
n = int(input("Enter a positive integer: "))
 
#Calculate the sum
total= n * (n+1) / 2
 
#Display the result
print("The sum of the first",n,"positive integers",total)



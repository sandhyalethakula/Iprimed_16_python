"""1.Write a program that reads a positive integer n, from the user and then displays the sum of all of the integers from 1 to n.
The sum of the first n positive integers can be computed using the formula:
sum=n(n+1)/2 """




n=int(input("enter any positive number"))                #takes a positive number from user
a=n*(n+1)/2                                               # formula to calculate sum of 1 to n positive integer
print("The sum of n positive numbers =",a)                #printing the answer

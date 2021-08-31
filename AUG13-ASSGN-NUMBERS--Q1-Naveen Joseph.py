'''1.Write a program that reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n.
The sum of the first n positive integers can be computed using the formula: sum = (n)(n + 1) / 2'''
n1=input("Enter a number : ")
n=int(n1)
n2 = n*(n+1)/2#formula for computing sum of the first n positive integers
print("The sum ofof all the natural numbers till ",n,'is',n2)

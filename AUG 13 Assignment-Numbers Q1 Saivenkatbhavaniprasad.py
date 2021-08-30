'''
1.Write a program that reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n. 
The sum of the first n positive integers can be computed using the formula: sum = (n)(n + 1) / 2 

'''

number = int(input('Enter a number >'))     #takes a number from the user
sum_value = (number)*(number + 1) / 2       #formula to calculate sum of number form 1 to given number without using for loop
print(int(sum_value))                       #prints sum of number, her int is used to print in int form not in float


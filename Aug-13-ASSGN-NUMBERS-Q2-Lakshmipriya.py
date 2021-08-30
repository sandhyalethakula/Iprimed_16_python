'''2.A retailer sells two products: Apples and Oranges. Each apple weighs 75 grams. Each orange weighs 112 grams.
Write a program that reads the number of apples and the number of oranges in an order from the user.
Then your program should compute and display the total weight of the order. '''

print('-'*20)
apples=int(input("Enter number of apples: "))   #Read the input from the user
oranges=int(input("Enter number of oranges: "))
total=(apples*75)+(oranges*112)#Calculate the sum
print("The total weight of the order of apples and oranges is",total)#Display the result
print('-'*20)

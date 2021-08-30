'''2.A retailer sells two products: Apples and Oranges. Each apple weighs 75 grams. Each orange weighs 112 grams.
Write a program that reads the number of apples and the number of oranges in an order from the user.
Then your program should compute and display the total weight of the order. '''

#total weight

apples=75
oranges=112

print("enter order:")
num_Apples=int(input("number of apples:"))
num_Oranges=int(input("number of oranges:"))

total_weight=num_Apples*apples+num_Oranges*oranges

print("Total weight is:",total_weight,"gm")



'''2.A retailer sells two products: Apples and Oranges. Each apple weighs 75 grams.
Each orange weighs 112 grams. Write a program that reads the number of apples and the number of oranges in an order from the user.
Then your program should compute and display the total weight of the order. 
'''
a=int(input("Enter the no. of apples you want : "))#the number of apples is taken from the user
b=int(input("Enter the no. of oranges that you want : "))#the number of oranges is taken from the user
tot=75*a+112*b#The formula to find the total weight
print ("The total weight of",a,"apples is : ",75*a,"grams ")
print ("The total weight of",b,"oranges is : ",112*b,"grams ")
print ("The total weight of fruits is : ",tot,"grams")

'''
A retailer sells two products: Apples and Oranges. Each apple weighs 75 grams.
Each orange weighs 112 grams.
Write a program that reads the number of apples and the number of oranges in an order from the user.
Then your program should compute and display the total weight of the order. 

'''
n1= input ("Enter the weight of apples: ")
n2 = input ("Enter the weight of oranges: ")

converts1 = int(n1) # converts number of widgets into an integer
convert2 = int(n2)  # converts number of gizmos into an integer

weightOfapples = converts1 * 75
weightOforanges = convert2 * 112


totalWeight = weightOfapples + weightOforanges

convert3 = str(totalWeight)
print ("") # prints an empty line
print ("The total weight of the order is " + convert3)

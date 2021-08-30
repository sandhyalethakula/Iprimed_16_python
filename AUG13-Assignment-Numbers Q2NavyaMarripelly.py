'''
3.A retailer sells two products: Apples and Oranges. Each apple weighs 75 grams. Each orange weighs 112 grams. Write a program that reads the number of apples and the number of oranges in an order from the user. Then your program should compute and display the total weight of the order. 
'''

no_of_oranges = int(input('Enter number of Oranges > ')) #Asks user to enter number of oranges
no_of_apples = int(input('Enter number of Apples > '))   #Asks user to enter number of apples
apple_weight =75                                         #weight in grams
orange_weight = 112                                      #weight in grams
total_weight = (no_of_oranges * orange_weight) + (no_of_apples * apple_weight)  #multiple no of oranges with weight same for apple
print('Total weight of both fruits is',total_weight,"grams")                                     #prints total weight for both apple and orange taken in grams

'''
3.A retailer sells two products: Apples and Oranges. Each apple weighs 75 grams. Each orange weighs 112 grams. Write a program that reads the number of apples and the number of oranges in an order from the user. Then your program should compute and display the total weight of the order. 
'''

oranges = int(input('Enter number of Oranges > ')) # enter number of oranges
apples = int(input('Enter number of Apples > '))   # enter number of apples
applewg =75                                        
orangewg = 112                                      
total = (oranges * orangewg) + (apples * applewg) 
print('Total weight of both fruits is',total) 

"""2.A retailer sells two products:apples and oranges . Each apple weighs 75 grams. Each orange weighs 112 grams. Write a program that reads the number
of oranges and apples in an order from the user. Then your program should compute and display the total weight of the order."""




a=int(input('enter the number of apples:'))                  #collecting the number of apples and oranges input from the user
o=int(input('enter the number of oranges:'))
wa= 75*a                                                    # multiplying the numbers of oranges and apples with their respective weights
wo= 112*o
total=wa+wo                                                   # adding both the values to the total weight and printing it
print("The total weight of apples and oranges=",total)       

            

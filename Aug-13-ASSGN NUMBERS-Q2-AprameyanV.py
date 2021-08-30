# A retailer sells two products: Apples and Oranges. Each apple weighs 75 grams.
# Each orange weighs 112 grams. Write a program that reads the number of apples
# and the number of oranges in an order from the user. Then your program
# should compute and display the total weight of the order.


a=75
b=112
a1=int(input("Enter the number of apples that you bought : "))
b1=int(input("Enter the number of oranges that you bought : "))
w=a*a1+b*b1
print ("The total weight of",a1,"apples is : ",a*a1,"grams ")
print ("The total weight of",b1,"oranges is : ",b*b1,"grams ")
print ("The total weight of fruits is : ",w,"grams ie;",w/1000,"Kg")
       

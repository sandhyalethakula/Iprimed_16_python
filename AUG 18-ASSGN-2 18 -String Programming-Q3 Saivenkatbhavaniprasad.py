''''
write a program that asks the user to enter two strings of the same length. The program should then check to see if 
the strings are of the same length. If they are not, the program should print an appropriate message and exit. If they 
are of the same length, the program should alternate the characters of the two strings. 
For example, if the user enters abcde and ABCDE the program should print out:
AaBbCcDdEe
'''
input1 = input("Enter a word >")
input2 = input("Enter a word >")                            #takes two inputs from the user with same lengths
d=0
if len(input1) != len(input2):
    print("You entered the wrong inputs!")                  #if length lenght of two inputs are not equal error raises
else:
    while d < len(input1):
        print(input1[d]+input2[d],end="")                   #if both lengths of input are equal it joins two words from the inputs at same index
        d+=1                                                #d increased by +1 for each loop to break loop and also increase the index value

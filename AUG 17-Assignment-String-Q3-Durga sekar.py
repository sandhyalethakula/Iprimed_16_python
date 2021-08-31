'''
3.Generate the pattern:
    5555555555
    44444444
    333333
    2222
    11
'''

num = int(input("Enter a number >"))            #takes input from users in numeric

while num > 0:
    print(str(num) * num*2)                     #prints each number * 2 with str(number) to generate required pattern
    num-=1                                      #number is subtracted by -1 for each loop to print each number and also to break loop



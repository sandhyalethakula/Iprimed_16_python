'''Write a program that asks the user to enter two strings of the same length. The program should then check to see if the strings are of the same length. If they are not, the program should print an appropriate message and exit. If they are of the same length, the program should alternate the characters of the two strings. 
For example, if the user enters abcde  and ABCDE  the program should print out: AaBbCcDdEe '''


def alternate_string(s1,s2):                                                      #  defined a function named alternate_string which accepts two strings as parameters#

    new_string=""                                                                      # created an empty string(new_string="")#

    if len(s1)==len(s2):                                                                    #len() function we check the length of two strings.#

        print("The two strings are of same length")

        for i in range(len(s1)):                                                #If they are equal then it will add the characters of the two strings alternately to the new_string using for loop#

            new_string=new_string+s2[i]+s1[i]

    else:

        print("The two strings are not of same length")                                            #if the length of two strings is not equal then the program will print an appropriate message#

    return new_string

string1=input("Enter string-1:")

string2=input("Enter string-2:")

print("New string is:",alternate_string(string1,string2))

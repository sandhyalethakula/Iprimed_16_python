'''
1.Ask the user to input And print the address neatly. 
	A. House number ? 
	B. Street info ? 
	C. Colony info ? 
	D. Landmark ? 
	E. City 
	F. Country 
	G. Pincode 
'''

house_num=input("Enter your house number >")        #asks user to enter house number
street_name=input("Enter your street info >")       #asks user to enter street info
colony_name=input("Enter your colony info >")       #asks user to enter colony info
landmark=input("Enter your landmark >")             #asks user to enter landmark
city=input("Enter your city name >")                #asks user to enter city name
country=input("Enter country name >")               #asks user to enter country name
pincode=input("Enter your city pincode >")          #asks user to enter city pincode

print("House number:- "+house_num, "Street info:- "+ street_name, "Colony info:- "+colony_name , "Landmar:- "+landmark,  "City:- "+city ,"pincode:- "+pincode,  "Country:- "+country, sep="\n")

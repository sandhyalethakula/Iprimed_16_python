"""Ask the user to enter their first name, middle name and last name and
print a mailing label using the consolidated name and address.""" 

first=input("enter the first name")
midlle=input("enter the middel name")
last=input("enter the last name")
house=input("enter your house number")
street=input("enter your street number")
colony=input("enter your colony name")
city=input("enter your city")
country=input("enter your country name")
pin=input("enter your locality pincode")
print("your name is ",first,midlle,last, "\nyour house no is" ,house,"\nyour street number is ",street,"\nColony number is",colony,
      "\nCity is",city,"\nCounty>", country, "\nPincode is" ,pin)

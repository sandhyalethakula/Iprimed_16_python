'''
2.Ask the user to enter their first name, middle name and last name and print a mailing label using the consolidated name and address. 
'''
house_num="12/24"
street_name="Godavari Bund"                         #Sample house_num,colony name, street name, city, pincode
colony_name ='Aryapuram'
city="Rajahmundry"
pincode='533104'
first_name=input("Enter your first name >")         #enter first name
middle_name=input("Enter your middle name >")       #enter middle name
last_name=input("Enter your last name >")           #enter last name

print("Mailing Address")
print("-"*20)
print(first_name,middle_name,last_name)             #prints full name
print(house_num, street_name,sep=', ')              #prints house number, streetname separated by ,
print(colony_name,',', city,pincode)           #prints colony name, city and pincode separated by ,


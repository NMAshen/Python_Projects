#name = input("Enter your name : ")
#phone_number = input("Enter your phone number")

#result = len(name) #Return length of Input
#result = name.find("a") #find where the specific character at
#result = name.rfind("a") #reverse find
#result = name.capitalize() #capitalize first letter
#result = name.upper() #all letters are get uppercase
#result = name.lower() #All letters are getting lowercase
#result = name.isdigit() #find is it a number then return true or false
#result = name.isalpha() # find is it a alphabatical letter then return true or false

#result = phone_number.count("-") #count how many dashes are there
#result = phone_number.replace("-", (" ")) #replace dashes with spaces



#print(result)

#----------------------------------------------------------------------------------------------------------------------------

#Excersice

name = input(str("Enter your Name : "))

if len(name) >= 12:
    print("Your user name is more than 12 characters")
elif name.find(" "):
    print("Your username can't contain any spaces")
elif not name.isalpha():
    print("Your username can't contain any numbers or symbols")
else :
    print(f"Welcome {name}")

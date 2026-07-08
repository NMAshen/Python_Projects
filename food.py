# using ++ operator
foods = input("if you like foods y/n :").lower()

if foods == "y" :
    print("Have some food")
elif foods == "n" :
    print("you dont get foods")
elif foods == "" :
    print("You didn't type anything")
else :
    print("Invalid input")
"""A while loop is a fundamental programming structure that tells your computer:
 "Keep repeating this block of code as long as this specific condition remains true."""

name = input("Enter your name : ")
age = int(input("Enter your age : "))

while name == (""):
    print("You haven't type anything")
    name = input("Enter your name : ")
print(f"Hi {name}")


while not age > 0:      # if age is lower than 0 this condition is true so it repeat
    print("You'r age can't be negative")
    age = int(input("Enter your age : "))
print(f"Your age is {age}")

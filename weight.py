# convert Kg to Lbs
weight = float(input("Enter your weight :"))
unit = input("Enter unit K/L :")

if unit == "K" :
    weight = weight * 2.205
    print(f"Your weight is {weight} Lbs")
elif unit == "L" :
    weight = weight / 2.205
    print(f"Your weight is {weight} Kg")
else :
    print(f"{unit} is invalid")
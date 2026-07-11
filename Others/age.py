age = int(input("Enter your age : "))

if age >= 18 :
    print("your an adult")
elif age <= -1 :
    print(f"you have to wait {abs(age)} years to born")
elif age <= 0 :
    print("you haven't even born yet")
else :
    print("your a child")

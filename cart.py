#shopping cart items price calculator
item = input("What item you buy : ")
price = float(input("How much is it : "))
quantity = int(input("how many items you buy : "))

total = price * quantity

print(f"your buying {quantity} {item}/s")
print(f"your total price is : {total}$")
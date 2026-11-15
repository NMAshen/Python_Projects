apple = 99.99
banana = -132.567
cake = 3.44

gta6 = 30000.00
minecraft = 10000

#print(f"Your price is {apple:.1f}") #.(how many decimal places to round)f

#print(f"Your item price is : {apple:>10}") # Right align 10 spaces
#print(f"Your item price is : {banana:<10}") #Left align
#print(f"Your item price is : {cake:^20}") #Center align

print(f"Your item price is : {apple:+}")  #Print + icon
print(f"Your item price is : {banana:+}")
print(f"Your item price is : {cake:+}")

print(f"{gta6:,}") #each thousends place replace with comma
print(f"{minecraft:,}")

print(f"{gta6:+,.2f}")

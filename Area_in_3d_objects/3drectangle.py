width = float(input("Enter your 3dRectanlge width: "))
height = float(input("Enter your 3dRectanlge height: "))
length = float(input("Enter your 3dRectanlge length: "))

area = 2* (width*height + width*length + length*height)

print(f"Your 3dRectangle area is {round(area, 2)}")

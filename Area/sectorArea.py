# Circle sector area

import math

radius = float(input("Enter radius of your circle :"))
degrees = int(input("Enter your sector degree :"))

area = math.pi * radius * radius * (degrees/360)

print(f"Your circle sector area is {round(area, 2)}")
# Calculator in Python..

import sys

fNum = (input("enter your first number :"))
if fNum == "":
    print("You haven't type the first number")
    sys.exit()

oper = (input("enter operator (+, -, *, /) :"))
if oper =="":
    print("Your haven't type the operator")
    sys.exit()

SNum = (input("enter your second number :"))
if SNum =="":
    print("You haven't type the Second number")
    sys.exit()
#----------------------------------------------------------------------------------------------------------------
fNum = float(fNum)
SNum = float(SNum)

if oper == "+":
        print(round(fNum + SNum, 2))
elif oper == "-":
        print(round(fNum - SNum, 2))
elif oper == "*":
        print(round(fNum * SNum, 2))
elif oper == "/":
            if SNum == 0:
                print("Can't divided by 0")
            else :
                print(round(fNum / SNum, 2))
else :
        print(f'"{oper}" is not a valid operator')


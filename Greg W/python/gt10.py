import random
y = 0
while y != 10:
    i = input ("Choose - or + to add or subtract 1")
    if i == "+":
        y = y + 1
        print(y)
    elif i == "-":
        y = y - 1
        print(y)
    if y == 5:
        print ("Keep going")
    if y == 1:
        print ("You are no where close")
    if y == 9:
        print ("This is as close as you can get without geting the number")
    
    
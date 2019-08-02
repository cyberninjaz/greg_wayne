i = input ("What operation do you choose?")
if i == "+":
    v = input("Enter a number")
    w = input("Enter a number")
    x = input("Enter a number")
    y = input("Enter a number")
    z = input("Enter a number")
    v = float (v)
    w = float (w)
    x = float (x)
    y = float (y)
    z = float (z)
    print (v+w+x+y+z)
elif i == "-":
    x = input ("Enter a number")
    y = input ("Enter a number")
    x = float (x)
    y = float (y)
    print (x-y)
elif i == "x":
    x = input ("Enter a number")
    y = input ("Enter a number")
    x = float (x)
    y = float (y)
    print (x*y)
elif i == "%":
    x = input ("Enter a number")
    y = input ("Enter a number")
    x = float (x)
    y = float (y)
    print (x/y)
else:
    print ("Does not compute, see inventor")





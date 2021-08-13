i = 0
while i == 0:  
    print()
    a = input ("Want to go? Type 'end' to end. ")
    if a == "yes":
        import random
        x = random.randint(1,1000)
        print(x)
        print()
    elif a == "no":
        print("Then why did you come here?")
        print()
        break
    elif a == "end":
        print("ended")
        print()
        break
    else:
        print("Not valid, try again.")
        print()
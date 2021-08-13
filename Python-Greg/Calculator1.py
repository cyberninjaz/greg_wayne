i = 0
while i == 0:
    print("")
    n1 = input ("Type in 1st number. Type 'end' to end -> ")
    if n1 == "end":
        print("ended")
        print()
        break
    print("+")
    print("-")
    print("x")
    print("%")
    op = input ("Select Operation. Type 'end' to end-> ")
    if op == "end":
        print("ended")
        print()
        break
    n2 = input ("Type in 2nd number. Type 'end' to end -> ")
    if n2 == "end":
        print("ended")
        print()
        break
    if op == "+":
        print(float(n1)+float(n2))
    elif op == "-":
        print(float(n1)-float(n2))
    elif op == "x":
        print(float(n1)*float(n2))
    elif op == "%":
        print(float(n1)/float(n2))
    else:
        print("Operation not valid")
    print()

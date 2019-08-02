print ("This is the future prediction machine")
i = input("What subject do you like best? Math, science, writing, or social science and buisness?")
if i == "Math":
    a = input ("Do you prefer economics in math or science in math?")
    if a == "Economics":
        print ("Theres no doubt in it. When you grow up you wil become a financial advisor.")
    elif a == "Science":
        b = input ("Would you like to use your knowlege to build machines or discover new things?")
        if b == "Build machines":
            print ("You will become a great engineer or a coder")
        elif b == "Discover new things":
            print ("You should become a physicist")
        else:
            print ("Does not compute. See inventor.")
    else:
        print ("Does not compute. See inventor.")
elif i == "Science":
    h = input ("Do you like medical science or natural science")
    if h == ("Medical science"):
        j = input ("Are you good in high pressure stituations?")
        if j == "Yes":
            print ("You may become either a surgeon or a nuclear medicine anisegiologist")
        elif j == "No":
            print ("You may become a standard doctor in an office or a pychiatrist.")
        else:
            print ("Does not compute. See inventor.")
    elif h == ("Natural science"):
        k = input (" Would you like something to do with nature or not.")
        if k == "Yes":
            print ("You will probably become with a biologist")
        if k == "No":
            print ("You may become a physicist or nuclear engineer")
        else:
            print ("Does not compute. See inventor.")
    else:
        print ("Does not compute. See inventor.")
elif i == "Writing":
    o = input ("Do like to write a lot or to do things relating to writing?")
    if o == "Write a lot":
        print ("You will become an author. Remember, with this job it is wise to have a backup.")
    elif o == "Do things relating to writing":
        p = input ("Do you like law?")
        if p == "Yes":
            print ("It is likely you will become a lawyer and if your good maybe a judge")
        elif p == "No":
            print ("You will be a great scribe")
        else:
            print ("Does not compute. See inventor.")
    print ("Does not compute. See inventor.")
elif i == "Social science and buisness":
    u = input ("Do you like social science or buisness")
    if u == "Social science":
        v = input ("Would you prefer education or politics?")
        if v == "eductation":
            w = input ("Would you like to teach or reasearch?")
            if w == "Teach":
                print ("You will become a teacher")
            if w == "Reasearch":
                print (" You will become an eductational reasearcher.")
            else:
                print ("Does not compute. See inventor.")
        elif v == "Politics":
            x = input ("Are you well known throughout the world")
            if x == "Yes":
                print ("You will be come a representative or senator. You may even become president!")
            elif x == "No":
                print ("You may become a congress member and hopefully a representative.")
            else:
                print ("Does not compute. See inventor.")
        print ("Does not compute. See inventor.")
    elif u == "Buisness":
        y = input ("Do you want to do things relating to buisness or start a buisness")
        if y == "Start a buisness":
            print ("You will become a buisness man")
        elif y == "Do things relating buisness":
            print ("You will become a financial advisor or a financial lawyer")
        else:
            print ("Does not compute. See inventor.")
    else:
        print ("Does not compute. See inventor.")
else:
    print ("Does not compute. See inventor.")
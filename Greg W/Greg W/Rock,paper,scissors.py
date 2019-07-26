while True:
    i=input("What do you play?")
    if i == "scissors":
        print (" I choose rock you lose ")
    elif i == "paper":
        print ( " I choose scissors you lose")
    elif i == "rock":
        print ( " I choose paper you lose")
    elif i == "quit":
        break 
    else:
        print (" you cheated, you lose")

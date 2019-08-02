print("This is the cheese church quiz to determine if you are loyal to the church or not. Ths will ask you a series of questions to determine the score.")
score = 0

a = input ("What cheese is the best?")
if a == "all cheese are created equal":
    print("Correct.Trick question. ")
    score = score + 1
else:
    print("All cheese are created equal")

b = input ("Do you think well of cheese?")
if b == "yes":
    print("Correct, cheese is good")
    score = score + 1
elif b == "no":
    print("INNCORRECT!")
else:
    print("Does not compute see inventor")

c = input ("Which one of these is not a real cheese. Barrel aged feta,sour d'fer, pico, or challerhocker.")
if c == "sour d'fer":
    print("Correct I made this up.")
    score = score + 1
else:
    print ("Inncorrect, that is a real cheese")

d = input ("What is the most stinky cheese on earth")
if d == "stinking bishop":
    print("Correct, this is the most stinky cheese known on earth.")
    score = score + 1
else:
    print("Not true")

e = input ("What is pasturization")
if e == "when dairy is sterilized":
    print("Correct, that is right")
    score = score + 1 
else:
    print("It is not that")

f = input ("What is the most popular cheese in the world")
if f == "mozzarella":
    print ("Good job!")
    score = score + 1
else:
    print("Inncorrect")

g = input ("Who brought cheese to America?")
if g == "the pilgrims":
    print ("Yes, the pilgrims brought cheese to America.")
    score = score + 1
else:
    print("No it wasn't them.")

g = input ("What is the pasture's name?")
if g == "pasture cyrus":
    print("Thats him.")
    score = score + 1
else:
    print("No, incorrect")

h = input ("What is the highest rank you can earn in church?")
if g == "grand master gouda":
    print("That's right")
    score = score + 1
else:
    print("Inncorrect")

i = input ("Who was the first to reach the title of Feta Father")
if g == "feta father chris":
    print("Correct")
    score = score + 1
else:
    print("Not true")

j = input ("When you start out what rank do you have?")
if j == "imsil initiate":
    print("Correct")
    score = score + 1
else:
    print("Inncorrect")

if score == 1:
    print("You scored 10 percent correct")
elif score == 2:
    print("You scored 20 percent correct")
elif score == 3:
    print("You scored 30 percent correct")
elif score == 4:
    print("You scored 40 percent correct")
elif score == 5:
    print("You scored 50 percent correct")
elif score == 6:
    print("You scored 60 percent correct")
elif score == 7:
    print("You scored 70 percent correct")
elif score == 8:
    print("You scored 80 percent correct")
elif score == 9:
    print("You scored 90 percent correct")
elif score == 10:
    print("Congradulations! You scored 100 percent correct!")
else:
    print("404")



    






    
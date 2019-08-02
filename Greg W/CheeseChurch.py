print ("Welcome to the Cheese Church quiz. This quiz will determine if you are able to join the church or not. This quiz will ask you a series of questi-ons to determine your score.")
print (" ")
print ("For a quick verification we have to ask you a question.")
aa = input ("Are you Piankhi?")
if aa == "yes":
    print ("Alert! Alert! System Shutdown!")
    break
elif aa == "no":
    print ("Moving on to the quiz.")

score = 0

print ("Question 1,")
a = input ("What type of cheese is the best? (please enter in lowercase letters) : ")
if a == "all cheese are created equal":
    print ("Correct. Trick question.")
    print (" ")
    score = score + 1
elif a == "all cheese are equal":
    print ("Correct. Trick question.")
    print (" ")
    score = score + 1
elif a == "cheese are equal":
    print ("Correct. Trick question.")
    print (" ")
    score = score + 1
else:
    print ("Incorrect.")
    print (" ")

print ("Question 2,")
print ("Do you think cheese is excellent, or do you think cheese is horrible?")
print ("a : Cheese is excellent.")
print ("b : Cheese is horrible.")
b = input ("Do you choose a, or b? (please enter in lowercase letters) : ")
if b == ("a"):
    print ("Correct!")
    print (" ")
    score = score + 1
elif b == ("b"):
    print ("INCORRECT!")
    print (" ")
else:
    print ("Error.")

print ("Question 3,")
print ("Which one of these is not a real cheese?")
print ("a : Barrel aged feta")
print ("b : Pico")
print ("c : Sour d'fer")
print ("d : Challerhocker")
c = input ("What do you choose? (please enter in lowercase letters) : ")
if c == "a":
    print ("Incorrect")
    print (" ")
elif c == "b":
    print ("Incorrect")
    print (" ")
elif c == "c":
    print ("Correct!")
    print (" ")
    score = score + 1
elif c == "d":
    print ("Incorrect")
    print (" ")
else:
    print ("Error.")

print ("Question 4,")
print ("What is the most popular cheese in the world?")
print ("a : Cheddar")
print ("b : Mozzerella")
print ("c : Brie")
print ("d : American Cheese")
d = input ("What do you choose? (please enter in lowercase letters) : ")
if d == "a":
    print ("Incorrect.")
    print (" ")
elif d == "b":
    print ("Correct!")
    print (" ")
    score = score + 1
elif d == "c":
    print ("Incorrect.")
    print (" ")
elif d == "d":
    print ("Incorrect.")
    print (" ")
else:
    print ("Error.")

print ("Question 5,")
print ("What is the stinkiest cheese in the world?")
print ("a : Blue Cheese")
print ("b : Aged Cheddar")
print ("c : Stinking Bishop")
print ("d : Stinking Mountain")
e = input ("What do you chose? (please enter in lowercase letters) : ")
if e == "a":
    print ("Incorrect.")
    print (" ")
elif e == "b":
    print ("Incorrect.")
    print (" ")
elif e == "c":
    print ("Correct!")
    print (" ")
    score = score + 1
elif e == "d":
    print ("Incorrect.")
    print (" ")
else:
    print ("Error.")

print ("Question 6,")
print ("Who brought cheese to America?")
print ("a : Christopher Columbus")
print ("b : Hernándo Cortés")
print ("c : The Irish")
print ("d : The Pilgrims")
f = input ("What do you chose? (please enter in lowercase letters) : ")
if f == "a":
    print ("Incorrect.")
    print (" ")
elif f == "b":
    print ("Incorrect.")
    print (" ")
elif f == "c":
    print ("Incorrect.")
    print (" ")
elif f == "d":
    print ("Correct!")
    print (" ")
    score = score + 1
else:
    print ("Error.")

print ("Question 7,")
print ("Who is the pasture of the Cheese Church?")
print ("a : Pasture Kris")
print ("b : Pasture Cyrus")
print ("c : Pasture Jakob")
print ("d : Pasture Holden")
g = input ("What do you chose? (please enter in lowercase letters) : ")
if g == "a":
    print ("Incorrect.")
    print (" ")
elif g == "b":
    print ("Correct!")
    print (" ")
    score = score + 1
elif g == "c":
    print ("Incorrect.")
    print (" ")
elif g == "d":
    print ("Incorrect.")
    print (" ")
else:
    print ("Error.")

print ("Question 8,")
print ("What is the highest rank you can earn in Cheese Church?")
print ("a : Guardian")
print ("b : Parmesan Paladin ")
print ("c : Gouda Grandmaster ")
print ("d : Feta Father ")
h = input ("What do you chose? (please enter in lowercase letters) : ")
if h == "a":
    print ("Incorrect.")
    print (" ")
elif h == "b":
    print ("Incorrect.")
    print(" ")
elif h == "c":
    print ("Correct!")
    print (" ")
    score = score + 1
elif h == "d":
    print ("Incorrect.")
    print (" ")
else:
    print ("Error.")

print ("Question 9,")
print ("Who was the first church member to reach the title of Feta Father?")
print ("a : Feta Father Atticus")
print ("b : Feta Father Ben")
print ("c : Feta Father Pratik")
print ("d : Feta Father Chris")
i = input ("What do you chose? (please enter in lowercase letters) : ")
if i == "a":
    print ("Incorrect.")
    print (" ")
elif i == "b":
    print ("Incorrect.")
    print (" ")
elif i == "c":
    print ("Incorrect.")
    print (" ")
elif i == "d":
    print ("Correct!")
    print (" ")
    score = score + 1
else:
    print ("Error.")

#Cheesus
print ("Question 10,")
print ("Who is the lord and savior of all.")
print ("a : Father Cheese")
print ("b : Cheesus")
print ("c : French Cheese Makers")
print ("d : The Cheese Angel")
j = input ("What do you chose? (please enter in lowercase letters) : ")
if j == "a":
    print ("Incorrect.")
    print (" ")
elif j == "b":
    print ("Correct!")
    print (" ")
    score = score + 1
elif j == "c":
    print ("Incorrect.")
    print (" ")
elif j == "d":
    print ("Incorrect.")
    print (" ")
else:
    print ("Error.")

if score <= 5:
    print ("You got "+ score +" out of 10 questions correct. ")
    print ("You got an F. You are not able to join the Cheese Church.")
if score == 6:
    print ("You got 6 out of 10 questions correct. ")
    print ("You got a D. You are not able to join the Cheese Church.")
if score == 7:
    print ("You got 7 out of 10 questions correct. ")
    print ("You got a C. You are not able to join the Cheese Church.")
if score == 8:
    print ("You got 8 out of 10 questionq correct. ")
    print ("You got a B. You are not able to join the Cheese Church. ")
if score == 9:
    print ("You got 9 out of 10 questions correct. ")
    print ("You got an A-. You will elgible to join the Cheese Church!")
if score == 10:
    print ("Congratulations! You scored 10 out of 10 questions correct!")
    print ("You earned an A+! You will definitely be accepted in the Cheese Church!")
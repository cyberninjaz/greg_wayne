
#Cheese Sauce


import random
import tkinter as tk

score = 0

x = 250
y = 250
speed = 5

ld= []
lc= []
ls= []

# CheeseSauce=[]

window = tk.Tk()

lbl=tk.Label(text="= The Cheese Game! =",font=("Cambria",20),bg="gold",width=33)
lbl.pack()

lbl=tk.Label(text="A Cheese Church Video Game",font=("Cambria",10),bg="orange",fg="black",width=71)
lbl.pack()

lbl=tk.Label(text="Press the Arrow Keys to Play!",font=("Cambria",10),bg="orange",fg="red",width=71)
lbl.pack()

lbl=tk.Label(text="Collect Cheese to Score Points!",font=("Cambria",10),bg="orange",fg="red",width=71)
lbl.pack()

lbl=tk.Label(text="Avoid The Vegan Cheese At All Costs!",font=("Cambria",10),bg="orange",fg="red",width=71)
lbl.pack()

lbl=tk.Label(text="Eat Spicy Cheese To Go Faster!",font=("Cambria",10),bg="orange",fg="red",width=71)
lbl.pack()

c = tk.Canvas(bg="silver",width=500,height=500)
cheese = tk.PhotoImage(file = "Cheese1.png")
minicheese = tk.PhotoImage(file = "Cheese2.png")
destroyer = tk.PhotoImage(file = "Cheese3.png")
spicycheese= tk.PhotoImage(file = "Cheese4.png")
c.pack()

lblt=tk.Label(text="Score:",width=71,bg="gold")
lblt.pack()

lbls=tk.Label(text=(score),width=71,bg="gold")
lbls.pack()

def DrawCheese ():
    c.create_rectangle(0,0,500,500,fill="silver")
    c.create_image(x,y, image = cheese)
    lbls.config(text=(score))
    for (mx,my) in lc:
        c.create_image(mx,my, image = minicheese)  
    for (dx,dy) in ld:
        c.create_image(dx,dy, image = destroyer) 
    for (sx,sy) in ls:
        c.create_image(sx,sy, image = spicycheese)


    # for (csx,csy) in CheeseSauce:
    #     c.create_rectangle(csx-5,csy-5,csx+5,csy+5,fill="gold",outline="gold")

def SpawnMiniCheese ():
    mx = random.randint(1,500)
    my = random.randint(1,500)
    lc.append((mx,my))
    DrawCheese()
    window.after(6000, SpawnMiniCheese)
window.after(0, SpawnMiniCheese)
    

def SpawnDestroyer ():
    dx = random.randint(1,500)
    dy = random.randint(1,500)
    ld.append((dx,dy))
    DrawCheese()
    window.after(6000, SpawnDestroyer)
window.after(0,SpawnDestroyer)

def SpawnSpicyCheese ():
    sx = random.randint(1,500)
    sy = random.randint(1,500)
    ls.append((sx,sy))
    DrawCheese()
    window.after(9000, SpawnSpicyCheese)
window.after(0,SpawnSpicyCheese)

    
def CheckCollision():
    global score
    for (mx,my) in lc:
        isColliding = True
        if (my) > (y+80):
            isColliding = False
        if (my+40) < (y):
            isColliding = False
        if (mx) > (x+80):
            isColliding = False
        if (mx+50) < (x):
            isColliding = False
        if isColliding:
            lc.remove((mx,my))
            score = score+10
            break

def CheckDestruction():
    for (dx,dy) in ld:
        isDestruction = True
        if (dy) > (y+80):
            isDestruction = False
        if (dy+60) < (y):
            isDestruction = False
        if (dx) > (x+80):
            isDestruction = False
        if (dx+60) < (x):
            isDestruction = False
        if isDestruction:
            c.pack_forget()
            lblGO=tk.Label(master=window, font=("Arial",20),bg="grey",fg="red",text="Game Over",width="31")
            lblGO.pack()
            break

def CheckFast():
    global speed
    for (sx,sy) in ls:
        isFast = True
        if (sy) > (y+80):
            isFast = False
        if (sy+50) < (y):
            isFast = False
        if (sx) > (x+80):
            isFast = False
        if (sx+50) < (x):
            isFast = False
        if isFast:
            speed=10
            def f():
                speed = 5
            window.after(10000, f)
            ls.remove((sx,sy))
            break
        

        

def Right (event):
    global x
    # CheeseSauce.append((x,y))
    # if len (CheeseSauce)>20:
    #     CheeseSauce.pop()
    x = x+speed
    CheckCollision()
    CheckDestruction()
    CheckFast()
    DrawCheese()

def Left (event):
    global x
    # CheeseSauce.append((x,y))
    # if len (CheeseSauce)>20:
    #     CheeseSauce.pop()
    x = x-speed
    CheckCollision()
    CheckDestruction()
    CheckFast()
    DrawCheese()

def Up (event):
    global y
    # CheeseSauce.append((x,y))
    # if len (CheeseSauce)>20:
    #     CheeseSauce.pop()
    y = y-speed
    CheckCollision()
    CheckDestruction()
    CheckFast()
    DrawCheese()

def Down (event):
    global y
    # CheeseSauce.append((x,y))
    # if len (CheeseSauce)>20:
    #     CheeseSauce.pop()
    y = y+speed
    CheckCollision()
    CheckDestruction()
    CheckFast()
    DrawCheese()


window.bind("<Left>",Left)
window.bind("<Right>",Right)
window.bind("<Up>",Up)
window.bind("<Down>",Down)


window.mainloop()

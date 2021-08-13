import random
import tkinter as tk

lpine= []
lveggie= []
lpep= []

window = tk.Tk()

lbl = tk.Label(font=("Times New Roman",30),text="-Pizza Maker-",width=50,bg="orange")
lbl.pack()

c=tk.Canvas(bg="black",width=1100,height=500)
pizza1=tk.PhotoImage(file="pizza3.png")
pizza2=tk.PhotoImage(file="Pizza2.png")
pizza3=tk.PhotoImage(file="pizza4.png")
c.pack()

def onClick1(event):
    PinePizza()
contPinePizza = True
def PinePizza ():
    for (x,y) in lpine:
        c.create_image(x,y, image = pizza1)  
    x = random.randint(1,1100)
    y = random.randint(1,500)
    lpine.append((x,y))
    if contPinePizza:
        window.after(10, PinePizza)

def onClick1S(event):
    global contPinePizza
    contPinePizza = False

def onClick2(event):
    VeggiePizza()
contVeggiePizza = True
def VeggiePizza ():
    for (x,y) in lveggie:
        c.create_image(x,y, image = pizza2)  
    x = random.randint(1,1100)
    y = random.randint(1,500)
    lveggie.append((x,y))
    if contVeggiePizza:
        window.after(10, VeggiePizza)

def onClick2S(event):
    global contVeggiePizza
    contVeggiePizza = False

def onClick3(event):
    PepPizza()
contPepPizza = True
def PepPizza ():
    for (x,y) in lpep:
        c.create_image(x,y, image = pizza3)  
    x = random.randint(1,1100)
    y = random.randint(1,500)
    lpep.append((x,y))
    if contPepPizza:
        window.after(10, PepPizza)

def onClick3S(event):
    global contPepPizza
    contPepPizza = False

Btn1 = tk.Button(text="Pineapple Pizza",bg="red",width=99,font=("Times New Roman",15))
Btn1.pack()

Btn1.bind("<Button-1>",onClick1)
Btn1.bind("<Button-3>",onClick1S)


Btn2 = tk.Button(text="Vegetable Pizza",bg="red",width=99,font=("Times New Roman",15))
Btn2.pack()

Btn2.bind("<Button-1>",onClick2)
Btn2.bind("<Button-3>",onClick2S)


Btn3 = tk.Button(text="Pepperoni Pizza",bg="red",width=99,font=("Times New Roman",15))
Btn3.pack()

Btn3.bind("<Button-1>",onClick3)
Btn3.bind("<Button-3>",onClick3S)

window.mainloop()
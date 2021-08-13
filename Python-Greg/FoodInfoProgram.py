import tkinter as tk
window = tk.Tk()

f = tk.Frame()
f.pack()

lbl=tk.Label(bg="orange",fg="red",font=("Cambria",30),text="-Food Info Program-", width=23)
lbl.pack()

lbl=tk.Label(bg="gold",fg="black",font=("Times New Roman",10),text="Hello! Welcome to the food learning program where you can learn about some delicious foods.",width=72)
lbl.pack()

lbl=tk.Label(bg="gold",fg="black",font=("Times New Roman",10),text="Select some of your favorite foods and learn all about them.",width=72)
lbl.pack()

pizza = tk.PhotoImage(file="Pizza1.png")
img = tk.Label(master=window,image=pizza)
img.pack(side=tk.TOP)


def onClick1 (event):
    lbl1=tk.Label(bg="navy",fg="gold",font=("Cambria",20),text="-Pizza-",width=34)
    lbl1.pack()
    lbl12=tk.Label(fg="black",font=("Times New Roman",10),width=72,text="Pizza is one of the most famous dishes in the world and almost everyone knows about it. \n There are many different kinds of pizza like pepperoni, cheese, vegetable, and many more. \n A simple pizza is also relatively easy to make, needing only dough, cheese, and tomato sauce. \n Pizza is truly one of the best foods in existence. ")
    lbl12.pack()
    BtnC1=tk.Button(text="Close",font=("Times New Roman",10),width=72)
    BtnC1.pack()
    def Close1 (event):
        lbl1.pack_forget()
        lbl12.pack_forget()
        BtnC1.pack_forget()
    BtnC1.bind("<Button-1>",Close1)


def onClick2 (event):
    lbl2=tk.Label(bg="navy",fg="gold",font=("Cambria",20),text="-Salmon-",width=34)
    lbl2.pack()
    lbl22=tk.Label(fg="black",font=("Times New Roman",10),width=72,text="Salmon is a tasty, pink fish that is great for eating. \n It is a great source of protein and it is very healthy. \n Salmon comes in dishes like sushi but it can still be great on its own. \n Put in some paprika, cumin, salt, and pepper to make your salmon excellent.")
    lbl22.pack()
    BtnC2=tk.Button(text="Close",font=("Times New Roman",10),width=72)
    BtnC2.pack()
    def Close2 (event):
        lbl2.pack_forget()
        lbl22.pack_forget()
        BtnC2.pack_forget()
    BtnC2.bind("<Button-1>",Close2)


def onClick3 (event):
    lbl3=tk.Label(bg="navy",fg="gold",font=("Cambria",20),text="-Aparagus-",width=34)
    lbl3.pack()
    lbl32=tk.Label(fg="black",font=("Times New Roman",10),width=72,text="Asparagus is a vegetable that comes in green stalks. \n It is nutricious, and it is special because the flavor depends a lot on how you cook it. \n Steaming asparagus my be suitable, but it is not nearly as good as asparagus sauteed in a pan\n with garlic and olive oil.")
    lbl32.pack()
    BtnC3=tk.Button(text="Close",font=("Times New Roman",10),width=72)
    BtnC3.pack()
    def Close3 (event):
        lbl3.pack_forget()
        lbl32.pack_forget()
        BtnC3.pack_forget()
    BtnC3.bind("<Button-1>",Close3)


def onClick4 (event):
    lbl4=tk.Label(bg="navy",fg="gold",font=("Cambria",20),text="-Breads-",width=34)
    lbl4.pack()
    lbl42=tk.Label(fg="black",font=("Times New Roman",10),width=72,text="Breads are one of the most common ways to eat grain. \n It can be made out of many grains like corn and rye though it usually is made from wheat. \n There also is a huge variety of breads like Italian bread, baguettes, sourdough,\n sandwich bread, and many more.")
    lbl42.pack()
    BtnC4=tk.Button(text="Close",font=("Times New Roman",10),width=72)
    BtnC4.pack()
    def Close4 (event):
        lbl4.pack_forget()
        lbl42.pack_forget()
        BtnC4.pack_forget()
    BtnC4.bind("<Button-1>",Close4)


def onClick5 (event):
    lbl5=tk.Label(bg="navy",fg="gold",font=("Cambria",20),text="-Fruit Salad-",width=34)
    lbl5.pack()
    lbl52=tk.Label(fg="black",font=("Times New Roman",10),width=72,text="Fruit Salad is a dish that consists of fruit and is extremely tasty. \n It also is relativiely easy to make. Just chop a bunch of fruit and put it in a bowl. \n Be sure to include melon, strawberry, blueberry,blackberry, rasberry, pineapple, and many more \ndelicious fruits.")
    lbl52.pack()
    BtnC5=tk.Button(text="Close",font=("Times New Roman",10),width=72)
    BtnC5.pack()
    def Close5 (event):
        lbl5.pack_forget()
        lbl52.pack_forget()
        BtnC5.pack_forget()
    BtnC5.bind("<Button-1>",Close5)

Btn1=tk.Button(width=72,text="Pizza")
Btn1.pack()

Btn1.bind("<Button-1>",onClick1)

Btn2=tk.Button(width=72,text="Salmon")
Btn2.pack()

Btn2.bind("<Button-1>",onClick2)

Btn3=tk.Button(width=72,text="Asparagus")
Btn3.pack()

Btn3.bind("<Button-1>",onClick3)

Btn4=tk.Button(width=72,text="Breads")
Btn4.pack()

Btn4.bind("<Button-1>",onClick4)

Btn5=tk.Button(width=72,text="Fruit Salad")
Btn5.pack()

Btn5.bind("<Button-1>",onClick5)

window.mainloop()
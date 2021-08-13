import tkinter as tk
window = tk.Tk()

car = tk.PhotoImage(file="car1.png",width=280,height=140)
img = tk.Label(master=window,image=car)
img.pack(side=tk.TOP)

f = tk.Frame(bg="navy")
f.pack()

lbl=tk.Label(master = f,text= "Can you drive?",width=35,height=10,font = ("Arial", 10),fg="Orange",bg="Navy")
lbl.pack()

lbl=tk.Label(master = f,text= "Enter your age.",width=35,height=3,font = ("Arial", 10),fg="Orange",bg="Grey")
lbl.pack()

Ent=tk.Entry(width=5)
Ent.pack()

def onClick (event):
    x = Ent.get()
    x = int(x)
    if x >= 16:
        lbl1 = tk.Label(bg="green",text="Get a license and then you can drive!",font = ("Arial", 10),width=35,height=3)
        lbl1.pack()
    elif x < 16:
        lbl2 = tk.Label(bg="red",text="Sorry, you can't drive yet.",font = ("Arial", 10),width=35,height=3)
        lbl2.pack()
    else:
        lbl3 = tk.Label(bg="blue",text="What you entered was not valid. Try again.",font = ("Arial", 10),width=35,height=3)
        lbl3.pack()

Btn=tk.Button(width=20,text="Click to see answer!")
Btn.pack()

Btn.bind("<Button-1>",onClick)

window.mainloop()


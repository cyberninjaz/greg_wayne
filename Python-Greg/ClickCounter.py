import tkinter as tk
window = tk.Tk()

f = tk.Frame(bg="navy")
f.pack()

press = tk.PhotoImage(file="CFinger.png")
img = tk.Label(master=window,image=press)
img.pack(side=tk.BOTTOM)

lbl=tk.Label(master = f,text="How Fast can you click?",bg="navy",fg="white",width=34)
lbl.pack()

lbl=tk.Label(master = f,text="Click the button and see the indicator.",bg="navy",fg="white",width=34)
lbl.pack()

x = 0

def onClick (event):
    global x
    x = x+1
    lbl.config(text=x)

Btn=tk.Button(width=20,text="Click me!")
Btn.pack()

Btn.bind("<Button-1>",onClick)

lbl=tk.Label(master = f,text= (x),bg="orange")
lbl.pack()

window.mainloop()
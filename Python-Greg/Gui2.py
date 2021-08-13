import tkinter as tk
window = tk.Tk()

f = tk.Frame(width=252)
f.pack()

lbl=tk.Label(master = f,text="Morning Sun")
lbl.pack()

sun = tk.PhotoImage(file="Sunrise Clipart.png")
img = tk.Label(master=window,image=sun)
img.pack(side=tk.TOP)

def onClick (event):
    img = tk.Label(master=window,image=sun)
    img.pack(side=tk.RIGHT) 

Btn=tk.Button(width=20,text="Click to get more!")
Btn.pack()

Btn.bind("<Button-1>",onClick)

window.mainloop()

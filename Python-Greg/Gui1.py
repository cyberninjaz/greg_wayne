import tkinter as tk
window = tk.Tk()

f = tk.Frame ()
f.pack()

lbl=tk.Label(master = f,text= "Hello",width = 100,height = 40)
lbl.pack()

window.mainloop()
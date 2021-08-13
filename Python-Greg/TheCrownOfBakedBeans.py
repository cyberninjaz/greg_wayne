import tkinter as tk
window = tk.Tk()

lbl=tk.Label(font=("Cambria",20),text="   =The Crown of Baked Beans=   ",bg="red",fg="gold")
lbl.pack()

c = tk.Canvas(bg="gold",height=420)

oval1 = c.create_oval(35,60,350,210,fill="orange")
oval2 = c.create_oval(65,90,320,180,fill="gold")

oval3 = c.create_oval(35,120,350,240,fill="orange")
oval4 = c.create_oval(65,150,320,210,fill="gold")

oval5 = c.create_oval(35,180,350,270,fill="orange")
oval6 = c.create_oval(65,210,320,240,fill="gold")

beans = tk.PhotoImage(file = "BakedBeans.png")
image = c.create_image(190,350,image=beans)

c.pack()

window.mainloop()
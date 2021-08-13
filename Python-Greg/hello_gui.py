import tkinter as tk

window = tk.Tk()
frame1 = tk.Frame(master=window)
frame1.pack(side=tk.TOP)
frame2 = tk.Frame(master=window)
frame2.pack(side=tk.TOP)

label = tk.Label(master=frame1, text="Would you like to play a game? ")
label.pack(side=tk.TOP)

entry = tk.Entry(master=frame2)
entry.pack(side=tk.LEFT)
button = tk.Button(master=frame2, text="Submit")
button.pack(side=tk.LEFT)

window.mainloop()

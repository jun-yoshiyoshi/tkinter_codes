import tkinter as tk


def return_press(event):
    en_val = strvar.get()
    print(en_val)
    strvar.set("enterd")


root = tk.Tk()
strvar = tk.StringVar()
en = tk.Entry(textvariable=strvar)
en.focus_set()
en.bind("<Return>", return_press)
en.pack()
root.mainloop()

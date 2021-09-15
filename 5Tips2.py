import tkinter as tk
# マウスイベントの割り当て


def callback_func(event):
    label["text"] = "x:{0},y{1}".format(event.x, event.y)


def callback_func1(event):
    button_num = event.num
    label1["text"] = "button num{0}".format(button_num)


root = tk.Tk()
root.geometry("300x300")
root.title("mouse x,y")

label = tk.Label(root, text="mouse", relief="groove")
root.bind("<Button-1>", callback_func)
label.pack()

label1 = tk.Label(root, text="button num", relief="groove")
root.bind("<Button>", callback_func1)
label1.pack()

root.mainloop()

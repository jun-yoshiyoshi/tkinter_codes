import tkinter as tk


def update_state(event):
    if boolvar.get() == 0:
        button["state"] = tk.ACTIVE
    else:
        button["state"] = tk.DISABLED


def enter_label(event):
    event.widget["background"] = "#bfb"


def leave_label(event):
    event.widget["background"] = "#bbf"


def callback_motion_func(event):
    label["fg"] = "black"
    label["text"] = "x:{0},y{1}".format(event.x, event.y)
# マウスを動かしているときのイベント


def callback_button_motion_func(event):
    label["fg"] = "red"
    label["text"] = "x:{0},y{1}".format(event.x, event.y)
# ボタンを押しながらマウスを動かしているときのイベント


def quit(event):
    if button["state"] == tk.ACTIVE:
        exit()


root = tk.Tk()
root.geometry("300x300")
root.title("mouse motion")


label = tk.Label(root, text="mouse motion, widget_en/le", relief="groove", background="#bbb")
label.pack(ipadx=50, pady=50)
label.bind("<Enter>", enter_label)
label.bind("<Leave>", leave_label)
root.bind("<Motion>", callback_motion_func)
root.bind("<Button1-Motion>", callback_button_motion_func)

boolvar = tk.BooleanVar()
checkbutton = tk.Checkbutton(text="はい、同意します", variable=boolvar)
checkbutton.pack(pady=5)
button = tk.Button(text="終了", state=tk.DISABLED)
button.pack(pady=5)
checkbutton.bind("<Button-1>", func=update_state)
button.bind("<Button-1>", func=quit)
[widget.pack(pady=10) for widget in (checkbutton, button)]

root.mainloop()

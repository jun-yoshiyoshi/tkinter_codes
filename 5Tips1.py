import tkinter as tk
# キーイベントの割り当て


def press_f1(event):
    label1["text"] = "pressed F1"


def callback_func(event):
    ks = event.keysym
    if ks == "Control_L" or ks == "Control_R":
        label2["text"] = "pressed control"
    else:
        label2["text"] = event.keysym
# Ctrl+c のようなショートカットは - を付け"<Control-c>" のようにします(または"<Control-Key-c>")。
# "<Control_L-c>" はエラーとなります。
# 左右で分けたい場合は"<Control_L><c>" のように連続押しで代用 。
# ただし、"<Control_L>" の後に"<c>"(連続であれば時間が空いても可)なので少しニュアンスが違ってくる。


root = tk.Tk()
root.geometry("300x150")
root.title("function key")
label1 = tk.Label(root, text="function key(F1)", relief="groove")
root.bind("<F1>", press_f1)
label1.pack()
label2 = tk.Label(root, text="key sym", relief="groove")
root.bind("<Key>", callback_func)
label2.pack()

root.mainloop()

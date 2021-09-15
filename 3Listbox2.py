import tkinter as tk


def set_allitem():
    # .select_set(2)でインデックス2を選択、.select_set(1,3)でインデックス1から3までを選択、.select_set(0, tkinter.END) で全選択
    listbox.select_set(0, tk.END)


def customed_select():
    # .size()で要素数を取得
    for i in range(1, listbox.size(), 2):
        listbox.select_set(i)
    #[listbox.select_set(i) for i in range(0,listbox.size()+1,2)]


def clear_item():
    listbox.select_clear(0, tk.END)


def delete_item():
    listbox.delete(0, tk.END)


root = tk.Tk()
root.geometry("200x200")
root.title("listbox set clear")
strvar = tk.StringVar(value=["北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州 沖縄"])
listbox = tk.Listbox(root, listvariable=strvar, selectmode="multiple", height=5)
button1 = tk.Button(text="全選択", command=set_allitem)
button2 = tk.Button(text="全解除", command=clear_item)
button3 = tk.Button(text="カスタム選択", command=customed_select)
button4 = tk.Button(text="全削除", command=delete_item)
[widget.pack() for widget in (listbox, button1, button2, button3, button4)]
root.mainloop()

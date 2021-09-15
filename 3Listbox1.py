import tkinter as tk


def get_listitem():
    print(listbox.curselection())


root = tk.Tk()
root.geometry("250x150")
root.title("get_listbox")
#strvar = tk.StringVar()
#strvar.set(["北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州", "沖縄"])

strvar = tk.StringVar(value=["北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州", "沖縄"])

listbox = tk.Listbox(root, listvariable=strvar, selectmode="multiple", height=5)
# 選択方式はbrowse,single,multiple,extendedの４種類
button = tk.Button(text="選択値を出力", command=get_listitem)

# 選択時の仮想イベント
listbox.bind("<<ListboxSelect>>", get_listitem)
# 選択 時 に 第 2 引数 に 指定 し た get_listitem 関数 が コール バック さ れる

[widget.pack() for widget in (listbox, button)]
root.mainloop()

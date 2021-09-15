import tkinter as tk
import tkinter.ttk as ttk


def get_comboitem(event):
    print(combobox.get())


root = tk.Tk()
root.geometry("280x150")
root.title("combobox event")
combobox = ttk.Combobox(root, values=("北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州 沖縄"))
# combobox.set("あらかじめ入力")
combobox.current(5)
# あらかじめ選択

# コンボ ボックス選択イベントは"<<ComboboxSelected>>" を渡す
combobox.bind("<<ComboboxSelected>>", get_comboitem)
# Enter 入力の有効化
combobox.bind("<Return>", get_comboitem)
combobox.pack()
root.mainloop()

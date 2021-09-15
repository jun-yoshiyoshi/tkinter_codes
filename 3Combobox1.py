import tkinter as tk
import tkinter.ttk as ttk


def get_comboitem():
    # .get()で取得する
    print(combobox.get())


root = tk.Tk()
root.geometry("280x150")
root.title("combobox")
# itemはvaluesにタプルで渡します
combobox = ttk.Combobox(root, values=("北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州 沖縄"))
combobox["state"] = "readonly"
# stateオプションはnormal,readonl,disableの三種類
button = tk.Button(text="入力/選択値を出力", command=get_comboitem)
combobox.pack()
button.pack()
root.mainloop()

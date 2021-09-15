import tkinter as tk


def action_bt_press():
    print("ボタンが押されました")


def print_txt_value():
    value_en = en.get()
    print(value_en)


root = tk.Tk()
root.title("text_boxコンテンツの取得")
root.geometry("350x150")
lb = tk.Label(text="ラベル")
en = tk.Entry()
bt = tk.Button(text="ボタン", command=action_bt_press)
bt_1 = tk.Button(text="ボタン_1", command=print_txt_value)

[widget. pack() for widget in (lb, en, bt, bt_1)]

root.mainloop()

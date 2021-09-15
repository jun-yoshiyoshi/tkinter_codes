import tkinter as tk


def print_txtval():
    # 内容 の 取得
    val_en = en.get()
    print(val_en)


def dele_txtval():
    val_dele = en.delete(0)
    # 末尾から削除する設定は不可
    print("最初の１文字を削除しました")


def alldele_txtval():
    val_alldele = en.delete(0, tk.END)
    # マイナスの設定は全て0と同じになった。
    print("全て削除しました")


def addhead_txtval():
    val_addhead = en.insert(0, "先頭に追加")


def insert3_txtval():
    val_insert3 = en.insert(3, "3の位置に追加")


def insertend_txtval():
    en.insert(tk.END, "最後に追加")


root = tk.Tk()
root.geometry("100x300")
# テキスト ボックス の 作成
en = tk.Entry()
en.focus_set()
# フォーカス を 当てる
bt_0 = tk.Button(text="ボタン0", command=print_txtval)
[widget.pack() for widget in (en, bt_0)]

bt_1 = tk.Button(text="ボタン1", command=dele_txtval)
[widget.pack() for widget in (en, bt_1)]

bt_2 = tk.Button(text="ボタン2", command=alldele_txtval)
[widget.pack() for widget in (en, bt_2)]

bt_3 = tk.Button(text="ボタン3", command=addhead_txtval)
[widget.pack() for widget in (en, bt_3)]

bt_4 = tk.Button(text="ボタン4", command=insert3_txtval)
[widget.pack() for widget in (en, bt_4)]

bt_5 = tk.Button(text="ボタン5", command=insertend_txtval)
[widget.pack() for widget in (en, bt_5)]

root.mainloop()

import tkinter as tk


def get_selpoint():
    # 選択 さ れ た 開始/ 終了 位置
    sel_start = tx.index("sel.first")
    sel_end = tx.index("sel.last")
    lb["text"] = "sel_start:{0}, sel_end:{1}".format(sel_start, sel_end)
    # 選択範囲の位置情報の取得（テキストそのものではない。）
    print(lb["text"])


def get_text():
    # 指定範囲のテキスト 取得
    sel_start = tx.index("sel.first")
    sel_end = tx.index("sel.last")
    print(tx. get(sel_start, sel_end))


def insert_cursor_point():
    # テキスト の 挿入
    tx.insert(tx.index("insert"), "+++++")


root = tk.Tk()
lb = tk.Label()
tx = tk.Text(width=30, height=5)
bt_0 = tk.Button(text="選択範囲", command=get_selpoint)
[widget.pack() for widget in (lb, tx, bt_0)]
bt_1 = tk.Button(text="選択範囲print", command=get_text)
[widget.pack() for widget in (lb, tx, bt_1)]
bt_2 = tk.Button(text="選択位置に挿入", command=insert_cursor_point)
[widget.pack() for widget in (lb, tx, bt_2)]

root.mainloop()

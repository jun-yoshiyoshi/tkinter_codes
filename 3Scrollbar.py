import tkinter as tk
root = tk.Tk()
root.title("Scrollbar Frame")
root.geometry("300x200")
# 1． フレーム を 作成 する
fr = tk.Frame(width=300, height=200)
fr.pack()
# 2． スクロールバー を 作成 する
sc = tk.Scrollbar(fr)
scx = tk.Scrollbar(fr, orient="horizontal")
# 3． スクロールバー を 配置 する 時 に side や fill で 位置 などを 指定 する
sc.pack(side=tk.RIGHT, fill="y")
scx.pack(side=tk.BOTTOM, fill="x")
# 4． 部品 を 作成 する
tx = tk.Text(fr)
tx["wrap"] = tk.NONE
tx.pack()
# 5． 部品 の 動き を スクロール バー に 反映 する よう に する
tx["yscrollcommand"] = sc.set
tx["xscrollcommand"] = scx.set
# 6． スクロールバー の 動き を 部品 に 反映 する よう に する
sc["command"] = tx.yview
scx["command"] = tx.xview
root.mainloop()

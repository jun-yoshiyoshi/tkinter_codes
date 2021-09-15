import tkinter as tk


def btn_press():
    print(" ボタン が 押さ れ まし た")


root = tk.Tk()
root.geometry("150x400")
# ボタン の 作成、 command オプション で 押 下 時 に 呼び出す 関数 を 指定 できる。
bt = tk.Button(text="ボタン", command=btn_press)
bt.pack()

bt_dict = {}
for bitmap_val in ["info", "error", "gray12", "gray25", "gray50", "gray75", "hourglass", "questhead", "question", "warning"]:
    # bitmap アイコン を つける こと も 出来る、 ここ では ループ で 種類 を 回し 表示
    bt_dict[bitmap_val] = tk.Button(bitmap=bitmap_val)
    bt_dict[bitmap_val].pack()

root. mainloop()

import tkinter as tk


def get_rdval():
    print(intvar.get())


def get_rdval1():
    print(strvar.get())


root = tk.Tk()
root.geometry("150x200")
root.title("Radiobutton")
intvar = tk.IntVar()
strvar = tk.StringVar()
# 初期 値 を セット
intvar.set(0)
strvar.set("z")
# ラジオ ボタン を 作成
rd1 = tk.Radiobutton(text="ラジオ 1", value=1, variable=intvar)
rd2 = tk.Radiobutton(text="ラジオ 2", value=2, variable=intvar)
bt = tk.Button(text="選択値を出力", command=get_rdval)

rdabc = tk.Radiobutton(text="ラジオ abc", value="abc", variable=strvar)
rddef = tk.Radiobutton(text="ラジオ def", value="def", variable=strvar)
bt1 = tk.Button(text="選択文字を出力", command=get_rdval1)
[widget.pack() for widget in (rd1, rd2, bt, rdabc, rddef, bt1)]
root.mainloop()

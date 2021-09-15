import tkinter as tk
import tkinter.ttk as ttk


def upd_scale(event=None):
    msessage["text"] = "callback\n{0}\n\nIntVar.get()\n{1}\n\nscale.get()\n{2}\n\nscale[\"value\"]\n{3}".format(
        event, var_scale.get(), scale.get(), scale["value"])


root = tk.Tk()
root.geometry("280x500")
root.title("scale")
msessage = tk.Message(root, width=500, aspect=300, text="scale value")
# 浮動小数点数 の 場合
# var_ scale = tk. DoubleVar()
var_scale = tk.IntVar()
# スケール の 作成
scale = ttk.Scale(root, from_=-10, to=10, variable=var_scale,
                  length=200, command=upd_scale, orient="vertical")
# from_=下限値　to=上限値
[widget.pack() for widget in (msessage, scale)]
var_scale.set(0)
root.mainloop()

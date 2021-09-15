import tkinter as tk
import random
root = tk.Tk()
root.title("pack")
# 位置
side_list = ["left", "right", "top", "bottom"]
# ランダムに配置してみる
label_list = []
for i in range(1, 31):
    side = side_list[random.randint(0, 3)]
    label_list.append(tk.Label(root, text="{0}:{1}".format("%02d" % i, side), relief="groove"))
    label_list[-1].pack(side=side)
root.mainloop()

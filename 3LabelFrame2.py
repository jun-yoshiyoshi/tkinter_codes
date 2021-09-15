import tkinter as tk
root = tk.Tk()
root.geometry("200x150")
root.title("labelanchor")
# ラベルの位置は８種類labelanchorで指定する
# 枠の種類は５種類
frame1 = tk.LabelFrame(root, text="n", labelanchor="n", relief="flat", width=60, height=40)
frame2 = tk.LabelFrame(root, text="ne", labelanchor="ne", relief="raised", width=60, height=40)
frame3 = tk.LabelFrame(root, text="e", labelanchor="e", relief="sunken", width=60, height=40)
frame4 = tk.LabelFrame(root, text="se", labelanchor="se", relief="groove", width=60, height=40)
frame5 = tk.LabelFrame(root, text="s", labelanchor="s", relief="ridge", width=60, height=40)
frame6 = tk.LabelFrame(root, text="sw", labelanchor="sw", relief="raised", width=60, height=40)
frame7 = tk.LabelFrame(root, text="w", labelanchor="w", relief="sunken", width=60, height=40)
frame8 = tk.LabelFrame(root, text="nw", labelanchor="nw", width=60, height=40)
# ラベルフレームで囲む範囲を指定
frame1.grid(column=1, row=0)
frame2.grid(column=2, row=0)
frame3.grid(column=2, row=1)
frame4.grid(column=2, row=2)
frame5.grid(column=1, row=2)
frame6.grid(column=0, row=2)
frame7.grid(column=0, row=1)
frame8.grid(column=0, row=0)


root.mainloop()

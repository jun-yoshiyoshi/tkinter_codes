import tkinter as tk
root = tk.Tk()
root.geometry("250x130")
root.title("LabelFrame")
# ラベル フレーム を 作成
frame = tk.LabelFrame(root, text="ラベル フレーム", foreground="#008800")
intvar = tk.IntVar()
intvar.set(0)
radio1 = tk.Radiobutton(frame, text="ラジオ１", value=1, variable=intvar)
radio2 = tk.Radiobutton(frame, text="ラジオ２", value=2, variable=intvar)
radio3 = tk.Radiobutton(frame, text="ラジオ３", value=3, variable=intvar)
[widget.pack() for widget in (frame, radio1, radio2, radio3)]

root.mainloop()

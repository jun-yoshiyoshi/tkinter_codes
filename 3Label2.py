import tkinter as tk

root = tk.Tk()
lb = tk.Label(text="MS ゴシック,サイズ20,太字,斜体,下線なし,取消線あり", font=(
    "ＭSゴシック", 20, "bold", "italic", "normal", "overstrike"))
lb.pack()
root.mainloop()

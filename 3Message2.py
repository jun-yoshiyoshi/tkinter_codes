import tkinter as tk
root = tk.Tk()
root.geometry("300x270")
ms_dict = {}
for bw_int in range(1, 6):
    bw_str = str(bw_int)
    # 枠 の 幅 は borderwidth を 使う、 ここ では ループ で 1 から 5 まで 設定
    ms_dict[bw_str] = tk.Message(text="borderwidth=" + bw_str, relief="ridge", bd=bw_int)
    ms_dict[bw_str].pack()
root. mainloop()

import tkinter as tk
root = tk.Tk()
root.geometry("600x400")
lb = tk.Label(text="This is a Label. This is a Label. \nThis is a Label.")
# メッセージ の 作成
ms = tk.Message(text="This is a Message. This is a Message. This is a \nMessage.", font=(40))
# font =(" Ｍ Ｓ ゴシック", 20, "normal", "italic", "normal", "overstrike"))

[widget.pack() for widget in (lb, ms)]

ms_dict = {}
for relief_val in ["flat", "raised", "sunken", "groove", "ridge"]:
    # 枠 の 種類 は relief を 使う、 ここ では ループ で 種類 を 回し 設定
    ms_dict[relief_val] = tk.Message(text=relief_val, relief=relief_val, bd=10)
    ms_dict[relief_val].pack()

root. mainloop()

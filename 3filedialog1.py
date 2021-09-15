import tkinter as tk
from tkinter import filedialog


def get_filepath():
    # 全てのファイルの場合
    filetype_list = [("all file", "*")]
    # .txtファイルの場合("text file", "*.txt"),.pyファイルの場合("py file", "*.py"),
    # ファイル パス の 取得
    filepath = filedialog.askopenfilename(
        initialdir="/home/suteab 12", filetypes=filetype_list, title="select file")
    # .askopenfilenames(),askopenfile(),.askopenfiles(),.asksabeasfilename(),.asksaveasfile(),.askdirectory()
    msessage["text"] = filepath


root = tk.Tk()
root.geometry("650x100")
root.title("filedialog")
msessage = tk.Message(root, text="file path", width=600)
button = tk.Button(text="get_filepath", command=get_filepath)
[widget.pack() for widget in (msessage, button)]
root.mainloop()

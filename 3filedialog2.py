import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog


def get_filepath():
    # .txt, .py, 全て の ファイル の 場合
    filetype_list = [("all file", "*")]
    # ("all file", "*")("text file", "*.txt"),("py file", "*.py"),
    # ただし、エンコーディングオプションが無いので、ファイルの種類によってはパスを取得してopen関数などで別に読み込む必要あり。
    # ファイル パス の 取得
    fileobj = filedialog.askopenfile(
        initialdir="/home/suteab12", filetypes=filetype_list, title="select file")
    if fileobj is not None:
        message["text"] = str(fileobj)
        content = fileobj.read()
        scrolledtext.insert(tk.END, content)
        fileobj.close()


root = tk.Tk()
root.geometry("650x300")
root.title("filedialog_read")
message = tk.Message(root, text="file path", width=600)
button = tk.Button(text="get_filepath", command=get_filepath)
scrolledtext = tksc.ScrolledText(root, height=10, width=70)
[widget.pack() for widget in (message, button, scrolledtext)]
root.mainloop()

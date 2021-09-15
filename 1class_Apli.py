import tkinter as tk
import tkinter.font as font


class Appli(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("text_box内容取得")
        master.geometry("350x150")
        master["highlightthickness"] = "7"
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lb = tk.Label(self)
        self.lb["text"] = "ラベル"

        self.lb.pack(side="top")
        self.en = tk.Entry(self)
        self.en.pack(side="left")
        self.en.focus_set()  # デフォルトで入力準備状態
        self.bt = tk.Button(self)
        self.bt["text"] = "ボタン"
        self.bt["command"] = self.print_txtvalue
        self.bt.pack(side="bottom")

    def print_txtvalue(self):
        value_en = self.en.get()
        print(value_en)


root = tk.Tk()
app = Appli(master=root)
app.mainloop()

import tkinter as tk
from tkinter import messagebox


def msg_info():
    label["text"] = str(messagebox.showinfo("info", "info message"))


def msg_warning():
    label["text"] = str(messagebox.showwarning("warning", "warning message"))


def msg_error():
    label["text"] = str(messagebox.showerror("error", "error message"))


def msg_question():
    label["text"] = str(messagebox.showquestion("question", "question message"))


def msg_yesno():
    label["text"] = label["text"] = "True(bool値)" if messagebox.askyesno(
        "yes/no", "yes/no message") else "False(bool値)"


def msg_okcancel():
    label["text"] = label["text"] = "True(bool値)" if messagebox.askokcancel(
        "ok/cancel", "ok/cancel message") else "False(bool値)"


def msg_retrycancel():
    label["text"] = label["text"] = "True(bool値)" if messagebox.askretrycancel(
        "retry/cancel", "retry/cancel message") else "False(bool値)"


root = tk.Tk()
root.geometry("650x100")
root.title("messagebox")
label = tk.Label(root, text="message result")
button_info = tk.Button(root, text="info", command=msg_info)
button_warning = tk.Button(root, text="warning", command=msg_warning)
button_error = tk.Button(root, text="error", command=msg_error)
button_question = tk.Button(root, text="question", command=msg_question)
button_yesno = tk.Button(root, text="yesno", command=msg_yesno)
button_okcancel = tk.Button(root, text="okcancel", command=msg_okcancel)
button_retrycancel = tk.Button(root, text="retrycancel", command=msg_retrycancel)
label.pack()
[widget.pack(side=tk.LEFT, padx=5) for widget in (button_info, button_warning,
                                                  button_error, button_question, button_yesno, button_okcancel, button_retrycancel)]
root.mainloop()

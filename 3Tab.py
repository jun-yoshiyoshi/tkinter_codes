import tkinter as tk
import tkinter.ttk as ttk


def press_button1():
    label1["text"] = "pressed button1"


def press_button2():
    label1["text"] = "pressed button2"


def chg_tab(event):
    print(notebook.select())


root = tk.Tk()
root.geometry("300x150")
root.title("Notebook")
notebook = ttk.Notebook(root)
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
notebook.add(tab1, text="tab1")
notebook.add(tab2, text="tab2")
notebook.pack(expand=True, fill="both")
label1 = tk.Label(tab1, text="tab1 label1")
button1 = tk.Button(tab1, text="tab1 button1", command=press_button1)
label2 = tk.Label(tab2, text="tab2 label2")
button2 = tk.Button(tab2, text="tab2 button2", command=press_button2)
[widget.pack(pady=10) for widget in (label1, button1, label2, button2)]
tabids = notebook.tabs()
print(tabids)
print(notebook.select())
notebook.bind("<<NotebookTabChanged>>", chg_tab)
notebook.select(tabids[1])
print(notebook.select())
root.mainloop()

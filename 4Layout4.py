import tkinter as tk
# 2次元配置
root = tk.Tk()
root.title("anchor")
root.geometry("500x200")
label1 = tk.Label(root, text="row=0,column=0", relief="groove", background="cyan")
label1.grid(row=0, column=0)
label2 = tk.Label(root, text="row=1,column=1", relief="groove", background="blue")
label2.grid(row=1, column=1)
label3 = tk.Label(root, text="row=3,column=3", relief="groove", background="white")
label3.grid(row=3, column=3)
label4 = tk.Label(root, text="row=0,column=4", relief="groove", background="yellow")
label4.grid(row=0, column=4)
label5 = tk.Label(root, text="row=5,column=1", relief="groove", background="green")
label5.grid(row=5, column=1)

root.mainloop()

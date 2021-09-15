import tkinter as tk
# レスポンシブ
root = tk.Tk()
root.title("anchor")
root.geometry("300x300")
label1 = tk.Label(root, text="text", relief="groove", background="cyan")
label1.pack()
label2 = tk.Label(root, text='anchor="se"', relief="groove", background="red")
label2.pack(anchor="se")
label3 = tk.Label(root, text='anchor="sw"', relief="groove", background="blue")
label3.pack(anchor="sw")
label4 = tk.Label(root, text='anchor="n"', relief="groove", background="green")
label4.pack(anchor="n")
label5 = tk.Label(root, text='anchor="nw"', relief="groove", background="white")
label5.pack(anchor="nw")
label6 = tk.Label(root, text='anchor="n"', relief="groove", background="black")
label6.pack(anchor="n")


root.mainloop()

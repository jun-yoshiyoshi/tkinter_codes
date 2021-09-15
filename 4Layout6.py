import tkinter as tk
# sticky ns/we　エクセルのセルの結合に近いイメージ
root = tk.Tk()
root.title("sticky")
root.geometry("500x500")
frame1 = tk.Frame(root, background="#eee")
# frame2 = tk.Frame(root, background="#fff")
label11 = tk.Label(frame1, text="r=1,c=0,rs=2, sticky=ns \n+++++++++\n++\n+++\n++++++++++",
                   relief="groove", background="cyan")
label11.grid(row=0, column=0, rowspan=5, sticky="ns")
label12 = tk.Label(frame1, text="r=2,c=1", relief="groove", background="blue")
label12.grid(row=2, column=1)
label13 = tk.Label(frame1, text="r=3,c=1\n+++++++++\n++\n+++++\n++++\n++++++++++++",
                   relief="groove", background="white")
label13.grid(row=3, column=1)
label14 = tk.Label(frame1, text="r=6,c=1\n+++++++++\n++\n+++++\n++++\n++++++++++++",
                   relief="groove", background="brown")
label14.grid(row=6, column=1)

frame1.pack(padx=10, pady=10)
#frame2.pack(padx=5, pady=5)
root.mainloop()

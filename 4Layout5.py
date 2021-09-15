import tkinter as tk
# rowspan/columnspan
root = tk.Tk()
root.title("frame padx=10 pady=10 grid:rowspan/columnspan")
root.geometry("500x500")
frame1 = tk.Frame(root, background="#ece")
# frame2 = tk.Frame(root, background="#cec")
label11 = tk.Label(frame1, text="rowspan=1,column=1 \n++++++++++++++++++++++++",
                   relief="groove", background="cyan")
label11.grid(rowspan=1, columnspan=1)
label12 = tk.Label(frame1, text="row=2,columnspan=2", relief="groove", background="blue")
label12.grid(row=2, columnspan=2)
label13 = tk.Label(frame1, text="row=2,column=3\n+++++++++\n++\n+++++\n++++\n++++++++++++",
                   relief="groove", background="white")
label13.grid(row=2, column=3)
label14 = tk.Label(frame1, text="row=6,column=6\n+++++++++\n++\n+++++\n++++\n++++++++++++",
                   relief="groove", background="brown")
label14.grid(row=6, column=6)

frame1.pack(padx=10, pady=10)
#frame2.pack(padx=5, pady=5)
root.mainloop()

import tkinter as tk
# widgetの余白
root = tk.Tk()
root.title("blank")

label = tk.Label(root, text="padx=100,pady=200,ipadx=20,ipady=40", background="cyan")
label.pack(padx=100, pady=200, ipadx=20, ipady=40)
root.mainloop()

# widgetの拡大
root1 = tk.Tk()
root1.title("Ｘ方向拡大")

label = tk.Label(root1, text="fill=x,pady=50,padx=5,++++++++++++", background="cyan")
label.pack(fill="x", padx=5, pady=50)
root1.mainloop()

root2 = tk.Tk()
root2.title("Y方向拡大")

labe2 = tk.Label(
    root2, text="fill=x,\npady=50,padx=5,\n+++++++\n++\n+++\nnoneは拡大しない\nbothは両方向とも拡大", background="cyan")
labe2.pack(fill="y", padx=5, pady=50)
root2.mainloop()

root3 = tk.Tk()
root3.title("responsible")

label = tk.Label(root3, text="responsible=True,\n++++++++\n+++++++++\n++++", background="cyan")
label.pack(fill="y", expand="True", pady=50)
root3.mainloop()

import tkinter as tk
# widgetの位置を指定して配置 place( x,y,width,height,relx,rely,relwidth,relheight)
root = tk.Tk()
root.title("sticky")
root.geometry("600x600")

frame1 = tk.Frame(root, width=600, height=300, background="#eee")
label11 = tk.Label(frame1, text="frame1 600x300\nrelx=0.25, rely=0.25\nrelwidth=0.5,relheight=0.5",
                   relief="groove", background="#fdf")
label11.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)

frame2 = tk.Frame(root, width=300, height=600, background="#fff")
label21 = tk.Label(frame2, text="frame2 300x600 x=50 y=50 \n width=150 height=150",
                   relief="groove", background="#ddf")
label21.place(x=50, y=50, width=150, height=150)

label22 = tk.Label(frame2, text="frame2 400x200 relx=0.5 rely=0.5 relwidth=0.25 relheight=0.25",
                   relief="groove", background="#ddf")
label22.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.25)

frame1.pack()
frame2.pack()


label14 = tk.Label(root, text="root,\nx=100\n y=100",
                   relief="groove", background="brown")
label14.place(x=100, y=100, width=50, height=50)

label15 = tk.Label(root, text="root,relx=0.5 rely=0.5 \n relwidth=0.25 \n++\n relheight=0.25\n+++",
                   relief="groove", background="brown")
label15.place(relx=0.5, rely=0.5, relwidth=0.25, relheight=0.25)


root.mainloop()

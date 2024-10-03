from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text="Hello world", variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="Hello python", variable=v, value=2).pack(anchor=W)
mainloop()
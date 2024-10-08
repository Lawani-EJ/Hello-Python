from tkinter import *
top = Tk()
mb = Menubutton (top, text = "Go and learn python!!")
mb.grid()
mb.menu = Menu (mb, tearoff = 0)
mb["menu"] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton (label = 'Contacts', variable=cVar)
mb.menu.add_checkbutton (label = 'About Us', variable=aVar)
mb.pack()
top.mainloop()
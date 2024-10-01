import tkinter as tk
r = tk.Tk()
r.title ("Whatever you do ... Please!! Don't click the button")
button = tk.Button(r, text="Click Me", width=28, command=r.destroy)
button.pack()
r.mainloop()
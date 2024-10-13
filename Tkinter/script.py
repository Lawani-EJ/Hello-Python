import tkinter as tk
root = tk.Tk()
root.title("Pack Examples")

button1 = tk.Button(root, text="This is the first button.")
button2 = tk.Button(root, text="This is the second button.")
button3 = tk.Button(root, text="This is the third button.")

button1.pack()
button2.pack()
button3.pack()
root.mainloop()
import tkinter as tk
root = tk.Tk()
root.title("Various Color Options Using tkinter. 👌")

button = tk.Button(root, text="Hi 🫢 Click ME!", activebackground="blue", activeforeground="white")
button.pack()

label = tk.Label(root,text= "Hello Friends😁😁", fg="black", bg="grey")
label.pack()

entry = tk.Entry(root, selectbackground="lightblue", selectforeground="black")
entry.pack()
root.mainloop()
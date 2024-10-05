import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

root = tk.Tk()
root.title("Combo Box Example..")

label = tk.Label(root, text="Selected Item: ")
label.pack(pady=10)

combo_box = ttk.Combobox(root, values=["Option 1", "Option2", "Option3"])
combo_box.pack(pady=5)

combo_box.set("Option1")
combo_box.bind("<<ComboBox Selected>>", on_select)

root.mainloop()
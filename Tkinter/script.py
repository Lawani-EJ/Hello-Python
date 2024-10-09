import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress.start()

    # simulating a task that takes time to complete
    for i in range(101):
        # simulating some work 
        time.sleep(0.05)
        progress['value'] = i
        # updating the UI 
        root.update_idletasks()
    progress.stop()

root = tk.Tk()
root.title("Progression Bar Implementation")

# creating the progression bar widget 
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=20)

# button to start progress
start_button = tk.Button(root, text="Click to start progression", command=start_progress)
start_button.pack(pady=10)

root.mainloop()
from tkinter import *
main = Tk()
ourMessage = "This Our New Message!!"
messageVar = Message(main, text=ourMessage)
messageVar.config(bg='red')
messageVar.pack() 
main.mainloop()
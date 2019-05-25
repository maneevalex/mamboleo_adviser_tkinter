from tkinter import *

root = Tk()
root.geometry('800x600')


frame = Frame(relief=RAISED, borderwidth=1)
frame.pack(fill=BOTH, expand=True)

closeButton = Button (text="Close")
closeButton.pack(side=RIGHT, padx=5, pady=5)


root.mainloop()
import tkinter as tk
import sqlite3
from datetime import datetime

class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        #Creating main window Labels

        self.name_lbl = tk.Label(self, text='Продажа абонементов', bg='lightgrey', fg='black',
                                 font=('Verdana', 14), width=66)
        self.name_lbl.grid(row=0, column=0, columnspan=4, ipady=10)
        self.name_lbl = tk.Label(self, text='Имя', fg='black', font=('Verdana', 14))
        self.name_lbl.grid(row=1, column=0, ipady=10, sticky=tk.W)
        self.name_lbl = tk.Label(self, text='Количество занятий', fg='black', font=('Verdana', 14))
        self.name_lbl.grid(row=2, column=0, ipady=10, sticky=tk.W)
        self.name_lbl = tk.Label(self, text='Стоимость', fg='black', font=('Verdana', 14))
        self.name_lbl.grid(row=3, column=0, ipady=10, sticky=tk.W)

        #Creating main window Buttons
        self.btn = tk.Button(self, text="Add to Database", command=self.submit, width=15, relief=tk.RAISED)
        self.btn.grid(row=3, column=3, sticky=tk.E, pady=10, ipady=7)
        self.btn = tk.Button(self, text="Close App", command=self.close_app, width=15, relief=tk.RAISED)
        self.btn.grid(row=4, column=3, sticky=tk.SE, pady=200, ipady=7)

        #Creating main window Entries
        self.entry = tk.Entry(self, width=50, font=('Monotype Corsiva', 14))
        self.entry.grid(row=1, column=1, columnspan=2, sticky=tk.W, ipady=8)
        self.entry1 = tk.Entry(self, width=50, font=('Monotype Corsiva', 14))
        self.entry1.grid(row=2, column=1, columnspan=2, sticky=tk.W, ipady=8)
        self.entry2 = tk.Entry(self, width=50, font=('Monotype Corsiva', 14))
        self.entry2.grid(row=3, column=1, columnspan=2, sticky=tk.W, ipady=8)


    def close_app(self):
        self.destroy()

    def submit(self):
        #Add to Database
        conn = sqlite3.connect('subscription.db')
        c = conn.cursor()

        c.execute("INSERT INTO subscription VALUES(:date, :name, :lessons, :cost)",
                {
                    "date": datetime.now().strftime("%B-%d %Y, %H:%m"),
                    "name": self.entry.get(),
                    "lessons": self.entry1.get(),
                    "cost": self.entry2.get(),
                })


        conn.commit()
        #Clear Entries
        self.entry.delete(0, tk.END)
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)

        #Close connection
        c.close()
        conn.close()

if __name__ == "__main__":
    root = Root()
    root.title('Mamboleo Adviser')
    root.geometry('800x600')
    root.resizable(False, False)
    root.mainloop()
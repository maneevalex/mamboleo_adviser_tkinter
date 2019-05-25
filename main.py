from tkinter import *
import sqlite3


root = Tk()
root.geometry('800x600')
main_font = ('Monotype Corsiva', 18)

def submit():
    #Connect DataBase
    conn = sqlite3.connect('subscription.db')
    c = conn.cursor()

    c.execute("INSERT INTO subscription VALUES(:name, :lesson, :money)",
              {
                  'name':name_entry.get(),
                  'lesson': lesson_entry.get(),
                  'money': money_entry.get()
              })

    conn.commit()
    c.close()

    name_entry.delete(0, END)
    lesson_entry.delete(0, END)
    money_entry.delete(0, END)


main_win_lbl = Label(root, text='Продажа абонементов', font=('Verdana', 20))
main_win_lbl.grid(row=0, column=1)

name_entry = Entry(root, width=30, font=main_font, borderwidth=2)
name_entry.grid(row=1, column=1, padx=10, pady=2, ipady=5, columnspan=2)
name_lbl = Label(root, font=main_font, text="Имя")
name_lbl.grid(row=1, column=0)

lesson_entry = Entry(root, width=30, font=main_font, borderwidth=2)
lesson_entry.grid(row=2, column=1, padx=10, pady=2, ipady=5, columnspan=2)
lesson_lbl = Label(root, font=main_font, text="Количество занятий")
lesson_lbl.grid(row=2, column=0)

money_entry = Entry(root, width=30, font=main_font, borderwidth=2)
money_entry.grid(row=3, column=1, padx=10, pady=2, ipady=5, columnspan=2)
name_lbl = Label(root, font=main_font, text="Стоимость")
name_lbl.grid(row=3, column=0)

submit_btn = Button(root, text='Сделать Запись', command=submit)
submit_btn.grid(row=4, column=1, ipady=2, pady=4, sticky=E)


root.mainloop()

conn = sqlite3.connect('subscription.db')
c = conn.cursor()
conn.commit()
c.close()
conn.close()

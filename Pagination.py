import tkinter as tk
import sqlite3
from datetime import datetime

class Casino_Adv(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        members = []
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("SELECT name FROM students")
        rows = c.fetchall()
        for row in rows:
            members.append(row)
        conn.commit()
        c.close()
        conn.close()


        self.list_box = tk.Listbox(self, selectmode=tk.MULTIPLE)
        self.list_box.insert(0, *members)
        self.list_box.pack()
        btn = tk.Button(self, text='Записать', command=self.add_data)
        btn.pack()

    def add_data(self):
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()
        clicked = self.list_box.curselection()
        for item in clicked:
        
            c.execute("INSERT INTO casino_adv VALUES(:name, :date)",
                      {
                          'name': ('').join(self.list_box.get(item)),
                          'date': datetime.now().strftime("%B-%d %Y")
                      })
            conn.commit()
        c.close()
        conn.close()

class Main(tk.Tk):

    def __init__(self):
        super().__init__()

        page = tk.Frame(self, bg='red')
        page.pack(side=tk.TOP, fill='both', expand=True)
        page.grid_rowconfigure(0, weight=1)
        page.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, StudentDataBase, PassRetailer, Schedule):
            frame = F(page, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.rowconfigure(0, weight=2)
        frame.columnconfigure(0, weight=2)
        frame.tkraise()

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Frame
        home_frame = tk.Frame(self)
        home_frame.pack(side="top", fill="both", expand=True)

        # Header Frame
        header_frame = tk.Frame(home_frame)
        header_frame.pack(side="top", fill="x", anchor="n")

        # Header Text
        label1 = tk.Label(header_frame, text="Главная", width=12, font="arial 16")
        label1.pack(side="left", padx=14, ipadx=20, ipady=10)

        #Schedule Page
        page_two_three = tk.Button(header_frame, text="Расписание", width=15, font="arial 11", relief=tk.RIDGE,
                                 border=3, command=lambda: controller.show_frame(Schedule))
        page_two_three.pack(side="right", padx=2, anchor="se")

        # PageTwo
        page_two_btn = tk.Button(header_frame, text="Продажа", width=15, font="arial 11", relief=tk.RIDGE,
                                 border=3, command=lambda: controller.show_frame(PassRetailer))
        page_two_btn.pack(side="right", padx=2, anchor="se")

        # PageOne
        page_one_btn = tk.Button(header_frame, text="База данных", width=17, relief=tk.RIDGE, border=3,
                                 font="arial 11", command=lambda: controller.show_frame(StudentDataBase))
        page_one_btn.pack(side="right", padx=2, anchor="se")



class StudentDataBase(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home_frame = tk.Frame(self)
        home_frame.pack(side="top", fill="both", expand=True)

        # Header Frame
        header_frame = tk.Frame(home_frame)
        header_frame.pack(side="top", fill="x", anchor="n")

        # Header Text
        label1 = tk.Label(header_frame, text="База Данных", width=12, font="arial 16")
        label1.pack(side="left", padx=14, ipadx=20, ipady=15)

        # Menu Buttons

        # Schedule Page
        page_two_three = tk.Button(header_frame, text="Расписание", width=15, font="arial 11", relief=tk.RIDGE,
                                   border=3, command=lambda: controller.show_frame(Schedule))
        page_two_three.pack(side="right", padx=2, anchor="se")

        # PageTwo
        page_two_btn = tk.Button(header_frame, text="Продажа", width=15, font="arial 11", relief=tk.RIDGE,
                                 border=3, command=lambda: controller.show_frame(PassRetailer))
        page_two_btn.pack(side="right", padx=2, anchor="se")

        # HomePage
        page_one_btn = tk.Button(header_frame, text="Главная", width=15, relief=tk.RIDGE, border=3,
                                 font="arial 11", command=lambda: controller.show_frame(HomePage))
        page_one_btn.pack(side="right", padx=2, anchor="se")

        #======================== Bottom Frame =================

        bottom_frame = tk.Frame(self, height=70)
        bottom_frame.pack(side=tk.BOTTOM, fill='x', expand=True, anchor='s')
        btn_add_record = tk.Button(bottom_frame, text='Добавить запись', width=15, font="arial 11",
                                   relief=tk.RIDGE, border=3, command=self.add_student_info)
        btn_add_record.grid(row=0, column=0, padx=20, pady=10)

        btn_clear_data = tk.Button(bottom_frame, text='Очистить данные', width=15, font="arial 11",
                                   relief=tk.RIDGE, border=3, command=self.clear_info)
        btn_clear_data.grid(row=0, column=1, padx=20, pady=10)


        #============================ Add Student ================

        student_frame = tk.Frame(self, width=700, height=500)
        student_frame.pack(side=tk.LEFT)
        self.name_label = tk.Label(student_frame, text='Имя', font=('Verdana', 20))
        self.name_label.grid(row=0, column=0, sticky=tk.NW, pady=12)
        self.name_label = tk.Label(student_frame, text='Контакт в ВК', font=('Verdana', 20))
        self.name_label.grid(row=1, column=0, sticky=tk.NW, pady=12)
        self.name_label = tk.Label(student_frame, text='Номер телефона', font=('Verdana', 20))
        self.name_label.grid(row=2, column=0, sticky=tk.NW, pady=12)
        self.name_label = tk.Label(student_frame, text='День рождения', font=('Verdana', 20))
        self.name_label.grid(row=3, column=0, sticky=tk.NW, pady=12)
        self.name_label = tk.Label(student_frame, text='Откуда узнал о нас', font=('Verdana', 20))
        self.name_label.grid(row=4, column=0, sticky=tk.NW, pady=12)

        self.name_info_entry = tk.Entry(student_frame, width=28, font=('Times New Roman', 20))
        self.name_info_entry.grid(row=0, column=1, padx=40, pady=12)
        self.vk_entry = tk.Entry(student_frame, width=28, font=('Times New Roman', 20))
        self.vk_entry.grid(row=1, column=1, padx=40, pady=12)
        self.telephone_entry = tk.Entry(student_frame, width=28, font=('Times New Roman', 20))
        self.telephone_entry.grid(row=2, column=1, padx=40, pady=12)
        self.birth_entry = tk.Entry(student_frame, width=28, font=('Times New Roman', 20))
        self.birth_entry.grid(row=3, column=1, padx=40, pady=12)
        self.root_entry = tk.Entry(student_frame, width=28, font=('Times New Roman', 20))
        self.root_entry.grid(row=4, column=1, padx=40, pady=12)

    def clear_info(self):
        self.name_info_entry.delete(0, tk.END)
        self.vk_entry.delete(0, tk.END)
        self.telephone_entry.delete(0, tk.END)
        self.birth_entry.delete(0, tk.END)
        self.root_entry.delete(0, tk.END)

    def add_student_info(self):
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("INSERT INTO students(name, vk_contact, telephone, birth, root) VALUES(:name, :vk_contact, :telephone, :birth, :root)",
                  {
                      "name": self.name_info_entry.get(),
                      "vk_contact": self.vk_entry.get(),
                      "telephone": self.telephone_entry.get(),
                      "birth": self.birth_entry.get(),
                      "root": self.root_entry.get(),
                  })

        conn.commit()
        # Clear Entries
        self.name_info_entry.delete(0, tk.END)
        self.vk_entry.delete(0, tk.END)
        self.telephone_entry.delete(0, tk.END)
        self.birth_entry.delete(0, tk.END)
        self.root_entry.delete(0, tk.END)

        # Close connection
        c.close()
        conn.close()



class PassRetailer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home_frame = tk.Frame(self)
        home_frame.pack(side="top", fill="both", expand=True)



        # Header Frame
        header_frame = tk.Frame(home_frame)
        header_frame.pack(side="top", fill="x", anchor="n")

        # Header Text
        label1 = tk.Label(header_frame, text="Продажа", width=12, font="arial 16")
        label1.pack(side="left", padx=14, ipadx=20, ipady=15)

        #Menu Buttons
        #HomePage
        # Schedule Page
        page_two_three = tk.Button(header_frame, text="Расписание", width=15, font="arial 11", relief=tk.RIDGE,
                                   border=3, command=lambda: controller.show_frame(Schedule))
        page_two_three.pack(side="right", padx=2, anchor="se", pady=10)

        # PageTwo
        page_two_btn = tk.Button(header_frame, text="База Данных", width=15, font="arial 11", relief=tk.RIDGE,
                                 border=3, command=lambda: controller.show_frame(StudentDataBase))
        page_two_btn.pack(side="right", padx=2, anchor="se", pady=10)

        # HomePage
        page_one_btn = tk.Button(header_frame, text="Главная", width=15, relief=tk.RIDGE, border=3,
                                 font="arial 11", command=lambda: controller.show_frame(HomePage))
        page_one_btn.pack(side="right", padx=2, anchor="se", pady=10)


        # ===========================Bottom Frame================

        bottom_frame = tk.Frame(self, height=70)
        bottom_frame.pack(side=tk.BOTTOM, fill='x', expand=True, anchor='s')

        btn_add_record = tk.Button(bottom_frame, text='Добавить запись', width=15, font="arial 11",
                                   relief=tk.RIDGE, border=3, command=self.submit_data)
        btn_add_record.grid(row=0, column=0, padx=20, pady=10)

        btn_clear_data = tk.Button(bottom_frame, text='Очистить данные', width=15, font="arial 11",
                                   relief=tk.RIDGE, border=3, command=self.clear_data)
        btn_clear_data.grid(row=0, column=1, padx=20, pady=10)

        btn_show_data = tk.Button(bottom_frame, text='Показать данные', width=15, font="arial 11",
                                   relief=tk.RIDGE, border=3, command=self.show_data)
        btn_show_data.grid(row=0, column=2, padx=20, pady=10)


        # ========================   Main Frame   =================

        main_frame = tk.Frame(self, width=800, height=500)
        main_frame.pack(side=tk.LEFT)

        self.name_label = tk.Label(main_frame, text='Имя', font=('Verdana', 25))
        self.name_label.grid(row=0, column=0, sticky=tk.NW, pady=12)
        self.name_label = tk.Label(main_frame, text='Абонемент', font=('Verdana', 25))
        self.name_label.grid(row=1, column=0, sticky=tk.NW, pady=12)
        self.name_label = tk.Label(main_frame, text='Стоимость', font=('Verdana', 25))
        self.name_label.grid(row=2, column=0, sticky=tk.NW, pady=12)

        self.name_entry = tk.Entry(main_frame, width=32, font=('Times New Roman', 20))
        self.name_entry.grid(row=0, column=1, padx=40, pady=12)
        self.type_entry = tk.Entry(main_frame, width=32, font=('Times New Roman', 20))
        self.type_entry.grid(row=1, column=1, padx=40, pady=12)
        self.cost_entry = tk.Entry(main_frame, width=32, font=('Times New Roman', 20))
        self.cost_entry.grid(row=2, column=1, padx=40, pady=12)

        #=========================   Info Frame   =======================

        info_frame = tk.Frame(self, width=800, height=500)
        info_frame.pack(side=tk.RIGHT)

        self.list_box = tk.Listbox(info_frame, width=600, height=300)
        self.list_box.pack()

    def clear_data(self):
            self.name_entry.delete(0, tk.END)
            self.type_entry.delete(0, tk.END)
            self.cost_entry.delete(0, tk.END)

    def submit_data(self):
        # Add to Database
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("INSERT INTO subscription VALUES(:date, :name, :lessons, :cost)",
                  {
                      "date": datetime.now().strftime("%B-%d %Y"),
                      "name": self.name_entry.get(),
                      "lessons": self.type_entry.get(),
                      "cost": self.cost_entry.get(),
                  })

        conn.commit()
        # Clear Entries
        self.name_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)
        self.cost_entry.delete(0, tk.END)

        # Close connection
        c.close()
        conn.close()

    def show_data(self):
        self.list_box.delete(0, tk.END)
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()
        c.execute("SELECT date, name, money FROM subscription ORDER BY date DESC")
        rows = c.fetchall()
        conn.commit()
        c.close()
        conn.close()
        for row in rows:
            self.list_box.insert(0, row)




class Schedule(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        home_frame = tk.Frame(self)
        home_frame.pack(side="top", fill="both", expand=True)

        # Header Frame
        header_frame = tk.Frame(home_frame)
        header_frame.pack(side="top", fill="x", anchor="n")

        # Header Text
        label1 = tk.Label(header_frame, text="Расписание", width=12, font="arial 16")
        label1.pack(side="left", padx=14, ipadx=20, ipady=15)

        #Menu Buttons
        #HomePage
        # Schedule Page
        page_two_three = tk.Button(header_frame, text="Продажа", width=17, font="arial 11", relief=tk.RIDGE,
                                   border=3, command=lambda: controller.show_frame(PassRetailer))
        page_two_three.pack(side="right", padx=2, anchor="se")

        # PageTwo
        page_two_btn = tk.Button(header_frame, text="База Данных", width=15, font="arial 11", relief=tk.RIDGE,
                                 border=3, command=lambda: controller.show_frame(StudentDataBase))
        page_two_btn.pack(side="right", padx=2, anchor="se")

        # HomePage
        page_one_btn = tk.Button(header_frame, text="Главная", width=17, relief=tk.RIDGE, border=3,
                                 font="arial 11", command=lambda: controller.show_frame(HomePage))
        page_one_btn.pack(side="right", padx=2, anchor="se")

        #================================= Manhattan Frame ================================

        manhattan_frame = tk.Frame(home_frame)
        manhattan_frame.pack(side=tk.LEFT)

        label = tk.Label(manhattan_frame, text="Понедельник", width=12, font="arial 16")
        label.grid(row=0, column=0, pady=15)
        label = tk.Label(manhattan_frame, text="Вторник", width=12, font="arial 16")
        label.grid(row=1, column=0, pady=15)
        label = tk.Label(manhattan_frame, text="Среда", width=12, font="arial 16")
        label.grid(row=2, column=0, pady=15)
        label = tk.Label(manhattan_frame, text="Четверг", width=12, font="arial 16")
        label.grid(row=3, column=0, pady=15)
        label = tk.Label(manhattan_frame, text="Пятница", width=12, font="arial 16")
        label.grid(row=4, column=0, pady=15)
        label = tk.Label(manhattan_frame, text="Суббота", width=12, font="arial 16")
        label.grid(row=5, column=0, pady=15)
        label = tk.Label(manhattan_frame, text="Воскресенье", width=12, font="arial 16")
        label.grid(row=6, column=0, pady=15)

        shedule_btn = tk.Button(manhattan_frame, width=17, text='Casino Adv // 18-30', command=self.open_casino)
        shedule_btn.grid(row=0, column=1, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='NY Beg // 19-30')
        shedule_btn.grid(row=0, column=2, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Rumba')
        shedule_btn.grid(row=0, column=3, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Bachata Int // 18-30')
        shedule_btn.grid(row=1, column=1, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Salsa Int // 19-30')
        shedule_btn.grid(row=1, column=2, padx=15)
        shedule_btn= tk.Button(manhattan_frame, width=17, text='Bachata Beg // 20-30')
        shedule_btn.grid(row=1, column=3, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Casino Adv // 18-30', command=self.open_casino)
        shedule_btn.grid(row=2, column=1, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='NY Beg // 19-30')
        shedule_btn.grid(row=2, column=2, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Female Style')
        shedule_btn.grid(row=2, column=3, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Bachata Int // 18-30')
        shedule_btn.grid(row=3, column=1, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Salsa Int // 19-30')
        shedule_btn.grid(row=3, column=2, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Bachata Beg // 20-30')
        shedule_btn.grid(row=3, column=3, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=4, column=1, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=4, column=2, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=4, column=3, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=5, column=1, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=5, column=2, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=5, column=3, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=6, column=1, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=6, column=2, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=6, column=3, padx=15)

        #================================= Malecon Frame =========================

        malecon_frame = tk.Frame(home_frame)
        malecon_frame.pack(side=tk.RIGHT)

        label = tk.Label(malecon_frame, text="Понедельник", width=12, font="arial 16")
        label.grid(row=0, column=0, pady=15)
        label = tk.Label(malecon_frame, text="Вторник", width=12, font="arial 16")
        label.grid(row=1, column=0, pady=15)
        label = tk.Label(malecon_frame, text="Среда", width=12, font="arial 16")
        label.grid(row=2, column=0, pady=15)
        label = tk.Label(malecon_frame, text="Четверг", width=12, font="arial 16")
        label.grid(row=3, column=0, pady=15)
        label = tk.Label(malecon_frame, text="Пятница", width=12, font="arial 16")
        label.grid(row=4, column=0, pady=15)
        label = tk.Label(malecon_frame, text="Суббота", width=12, font="arial 16")
        label.grid(row=5, column=0, pady=15)
        label = tk.Label(malecon_frame, text="Воскресенье", width=12, font="arial 16")
        label.grid(row=6, column=0, pady=15)

        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=0, column=1, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=0, column=2, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=0, column=3, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=1, column=1, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=1, column=2, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=1, column=3, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=2, column=1, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=2, column=2, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=2, column=3, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=3, column=1, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=3, column=2, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=3, column=3, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=4, column=1, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=4, column=2, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=4, column=3, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=5, column=1, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=5, column=2, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=5, column=3, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=6, column=1, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=6, column=2, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Тут занятие')
        shedule_btn.grid(row=6, column=3, padx=15)


    def open_casino(self):
        casino_adv = Casino_Adv(self)
        casino_adv.grab_set()
        casino_adv.geometry('800x600')
        casino_adv.title('Casino Advanced 18-30')



if __name__ == "__main__":
    root = Main()
    root.geometry('1300x680+0+0')

    root.mainloop()

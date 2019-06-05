import tkinter as tk
import sqlite3
from datetime import datetime

class Casino_Adv(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        main_frame = tk.Frame(self)
        main_frame.pack(fill='both', expand=True)

        left_frame = tk.Frame(main_frame, height=100, width=100)
        left_frame.pack(side=tk.LEFT)


        members = []
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("SELECT name FROM students WHERE casino_adv=1")
        rows = c.fetchall()
        for row in rows:
            members.append(row)
        conn.commit()
        c.close()
        conn.close()


        self.list_box = tk.Listbox(left_frame, selectmode=tk.MULTIPLE, height=30)
        self.list_box.insert(0, *members)
        self.list_box.grid(row=0, column=0)
        btn = tk.Button(left_frame, text='Записать', command=self.add_data)
        btn.grid(row=0, column=2)

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


class Rueda(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        main_frame = tk.Frame(self)
        main_frame.pack(fill='both', expand=True)

        left_frame = tk.Frame(main_frame, height=100, width=100)
        left_frame.pack(side=tk.LEFT)

        members = []
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("SELECT name FROM students WHERE rueda=1")
        rows = c.fetchall()
        for row in rows:
            members.append(row)
        conn.commit()
        c.close()
        conn.close()

        self.list_box = tk.Listbox(left_frame, selectmode=tk.MULTIPLE, height=30)
        self.list_box.insert(0, *members)
        self.list_box.grid(row=0, column=0)
        btn = tk.Button(left_frame, text='Записать', command=self.add_data)
        btn.grid(row=0, column=2)

    def add_data(self):
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()
        clicked = self.list_box.curselection()
        for item in clicked:
            c.execute("INSERT INTO rueda VALUES(:name, :date)",
                      {
                          'name': ('').join(self.list_box.get(item)),
                          'date': datetime.now().strftime("%B-%d %Y")
                      })
            conn.commit()
        c.close()
        conn.close()

class Rumba(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        main_frame = tk.Frame(self)
        main_frame.pack(fill='both', expand=True)

        left_frame = tk.Frame(main_frame, height=100, width=100)
        left_frame.pack(side=tk.LEFT)

        members = []
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("SELECT name FROM students WHERE rumba=1")
        rows = c.fetchall()
        for row in rows:
            members.append(row)
        conn.commit()
        c.close()
        conn.close()

        self.list_box = tk.Listbox(left_frame, selectmode=tk.MULTIPLE, height=30)
        self.list_box.insert(0, *members)
        self.list_box.grid(row=0, column=0)
        btn = tk.Button(left_frame, text='Записать', command=self.add_data)
        btn.grid(row=0, column=2)

    def add_data(self):
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()
        clicked = self.list_box.curselection()
        for item in clicked:
            c.execute("INSERT INTO rumba VALUES(:name, :date)",
                      {
                          'name': ('').join(self.list_box.get(item)),
                          'date': datetime.now().strftime("%B-%d %Y")
                      })
            conn.commit()
        c.close()
        conn.close()

class NY_Adv(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        main_frame = tk.Frame(self)
        main_frame.pack(fill='both', expand=True)

        left_frame = tk.Frame(main_frame, height=100, width=100)
        left_frame.pack(side=tk.LEFT)

        members = []
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("SELECT name FROM students WHERE ny_adv=1")
        rows = c.fetchall()
        for row in rows:
            members.append(row)
        conn.commit()
        c.close()
        conn.close()

        self.list_box = tk.Listbox(left_frame, selectmode=tk.MULTIPLE, height=30)
        self.list_box.insert(0, *members)
        self.list_box.grid(row=0, column=0)
        btn = tk.Button(left_frame, text='Записать', command=self.add_data)
        btn.grid(row=0, column=2)

    def add_data(self):
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()
        clicked = self.list_box.curselection()
        for item in clicked:
            c.execute("INSERT INTO ny_adv VALUES(:name, :date)",
                      {
                          'name': ('').join(self.list_box.get(item)),
                          'date': datetime.now().strftime("%B-%d %Y")
                      })
            conn.commit()
        c.close()
        conn.close()


class Casino_New(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        main_frame = tk.Frame(self)
        main_frame.pack(fill='both', expand=True)

        left_frame = tk.Frame(main_frame, height=100, width=100)
        left_frame.pack(side=tk.LEFT)

        members = []
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("SELECT name FROM students WHERE casino_new=1")
        rows = c.fetchall()
        for row in rows:
            members.append(row)
        conn.commit()
        c.close()
        conn.close()

        self.list_box = tk.Listbox(left_frame, selectmode=tk.MULTIPLE, height=30)
        self.list_box.insert(0, *members)
        self.list_box.grid(row=0, column=0)
        btn = tk.Button(left_frame, text='Записать', command=self.add_data)
        btn.grid(row=0, column=2)

    def add_data(self):
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()
        clicked = self.list_box.curselection()
        for item in clicked:
            c.execute("INSERT INTO rumba VALUES(:name, :date)",
                      {
                          'name': ('').join(self.list_box.get(item)),
                          'date': datetime.now().strftime("%B-%d %Y")
                      })
            conn.commit()
        c.close()
        conn.close()


class NY_New(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        main_frame = tk.Frame(self)
        main_frame.pack(fill='both', expand=True)

        left_frame = tk.Frame(main_frame, height=100, width=100)
        left_frame.pack(side=tk.LEFT)

        members = []
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("SELECT name FROM students WHERE ny_new=1")
        rows = c.fetchall()
        for row in rows:
            members.append(row)
        conn.commit()
        c.close()
        conn.close()

        self.list_box = tk.Listbox(left_frame, selectmode=tk.MULTIPLE, height=30)
        self.list_box.insert(0, *members)
        self.list_box.grid(row=0, column=0)
        btn = tk.Button(left_frame, text='Записать', command=self.add_data)
        btn.grid(row=0, column=2)

    def add_data(self):
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()
        clicked = self.list_box.curselection()
        for item in clicked:
            c.execute("INSERT INTO ny_new VALUES(:name, :date)",
                      {
                          'name': ('').join(self.list_box.get(item)),
                          'date': datetime.now().strftime("%B-%d %Y")
                      })
            conn.commit()
        c.close()
        conn.close()

class Bachata_Int(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        main_frame = tk.Frame(self)
        main_frame.pack(fill='both', expand=True)

        left_frame = tk.Frame(main_frame, height=100, width=100)
        left_frame.pack(side=tk.LEFT)

        members = []
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("SELECT name FROM students WHERE bachata_int=1")
        rows = c.fetchall()
        for row in rows:
            members.append(row)
        conn.commit()
        c.close()
        conn.close()

        self.list_box = tk.Listbox(left_frame, selectmode=tk.MULTIPLE, height=30)
        self.list_box.insert(0, *members)
        self.list_box.grid(row=0, column=0)
        btn = tk.Button(left_frame, text='Записать', command=self.add_data)
        btn.grid(row=0, column=2)

    def add_data(self):
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()
        clicked = self.list_box.curselection()
        for item in clicked:
            c.execute("INSERT INTO bachata_int VALUES(:name, :date)",
                      {
                          'name': ('').join(self.list_box.get(item)),
                          'date': datetime.now().strftime("%B-%d %Y")
                      })
            conn.commit()
        c.close()
        conn.close()

class Casino_Int(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        main_frame = tk.Frame(self)
        main_frame.pack(fill='both', expand=True)

        left_frame = tk.Frame(main_frame, height=100, width=100)
        left_frame.pack(side=tk.LEFT)

        members = []
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("SELECT name FROM students WHERE casino_int=1")
        rows = c.fetchall()
        for row in rows:
            members.append(row)
        conn.commit()
        c.close()
        conn.close()

        self.list_box = tk.Listbox(left_frame, selectmode=tk.MULTIPLE, height=30)
        self.list_box.insert(0, *members)
        self.list_box.grid(row=0, column=0)
        btn = tk.Button(left_frame, text='Записать', command=self.add_data)
        btn.grid(row=0, column=2)

    def add_data(self):
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()
        clicked = self.list_box.curselection()
        for item in clicked:
            c.execute("INSERT INTO casino_int VALUES(:name, :date)",
                      {
                          'name': ('').join(self.list_box.get(item)),
                          'date': datetime.now().strftime("%B-%d %Y")
                      })
            conn.commit()
        c.close()
        conn.close()

class Bachata_New(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        main_frame = tk.Frame(self)
        main_frame.pack(fill='both', expand=True)

        left_frame = tk.Frame(main_frame, height=100, width=100)
        left_frame.pack(side=tk.LEFT)

        members = []
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("SELECT name FROM students WHERE bachata_new=1")
        rows = c.fetchall()
        for row in rows:
            members.append(row)
        conn.commit()
        c.close()
        conn.close()

        self.list_box = tk.Listbox(left_frame, selectmode=tk.MULTIPLE, height=30)
        self.list_box.insert(0, *members)
        self.list_box.grid(row=0, column=0)
        btn = tk.Button(left_frame, text='Записать', command=self.add_data)
        btn.grid(row=0, column=2)

    def add_data(self):
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()
        clicked = self.list_box.curselection()
        for item in clicked:
            c.execute("INSERT INTO bachata_new VALUES(:name, :date)",
                      {
                          'name': ('').join(self.list_box.get(item)),
                          'date': datetime.now().strftime("%B-%d %Y")
                      })
            conn.commit()
        c.close()
        conn.close()

class Female_Style(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        main_frame = tk.Frame(self)
        main_frame.pack(fill='both', expand=True)

        left_frame = tk.Frame(main_frame, height=100, width=100)
        left_frame.pack(side=tk.LEFT)

        members = []
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("SELECT name FROM students WHERE female_style=1")
        rows = c.fetchall()
        for row in rows:
            members.append(row)
        conn.commit()
        c.close()
        conn.close()

        self.list_box = tk.Listbox(left_frame, selectmode=tk.MULTIPLE, height=30)
        self.list_box.insert(0, *members)
        self.list_box.grid(row=0, column=0)
        btn = tk.Button(left_frame, text='Записать', command=self.add_data)
        btn.grid(row=0, column=2)

    def add_data(self):
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()
        clicked = self.list_box.curselection()
        for item in clicked:
            c.execute("INSERT INTO female_style VALUES(:name, :date)",
                      {
                          'name': ('').join(self.list_box.get(item)),
                          'date': datetime.now().strftime("%B-%d %Y")
                      })
            conn.commit()
        c.close()
        conn.close()

class NY_Int(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        main_frame = tk.Frame(self)
        main_frame.pack(fill='both', expand=True)

        left_frame = tk.Frame(main_frame, height=100, width=100)
        left_frame.pack(side=tk.LEFT)

        members = []
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("SELECT name FROM students WHERE ny_int=1")
        rows = c.fetchall()
        for row in rows:
            members.append(row)
        conn.commit()
        c.close()
        conn.close()

        self.list_box = tk.Listbox(left_frame, selectmode=tk.MULTIPLE, height=30)
        self.list_box.insert(0, *members)
        self.list_box.grid(row=0, column=0)
        btn = tk.Button(left_frame, text='Записать', command=self.add_data)
        btn.grid(row=0, column=2)

    def add_data(self):
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()
        clicked = self.list_box.curselection()
        for item in clicked:
            c.execute("INSERT INTO ny_int VALUES(:name, :date)",
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

    #=================================   Right Frame   =================

        right_frame = tk.Frame(self, width=700, height=500)
        right_frame.pack(side=tk.RIGHT)
        self.ch1 = tk.BooleanVar()
        self.ch2 = tk.BooleanVar()
        self.ch3 = tk.BooleanVar()
        self.ch4 = tk.BooleanVar()
        self.ch5 = tk.BooleanVar()
        self.ch6 = tk.BooleanVar()
        self.ch7 = tk.BooleanVar()
        self.ch8 = tk.BooleanVar()
        self.ch9 = tk.BooleanVar()
        self.ch10 = tk.BooleanVar()
        self.ch11 = tk.BooleanVar()
        ch_1 = tk.Checkbutton(right_frame, text='Casino New', variable=self.ch1, width=20)
        ch_2 = tk.Checkbutton(right_frame, text='Casino Int', variable=self.ch2, width=20)
        ch_3 = tk.Checkbutton(right_frame, text='Casino Adv', variable=self.ch3, width=20)
        ch_4 = tk.Checkbutton(right_frame, text='SalsaOn2 New', variable=self.ch4, width=20)
        ch_5 = tk.Checkbutton(right_frame, text='SalsaOn2 Int', variable=self.ch5, width=20)
        ch_6 = tk.Checkbutton(right_frame, text='SalsaOn2 Adv', variable=self.ch6, width=20)
        ch_7 = tk.Checkbutton(right_frame, text='Bachata New', variable=self.ch7, width=20)
        ch_8 = tk.Checkbutton(right_frame, text='Bachata Int', variable=self.ch8, width=20)
        ch_9 = tk.Checkbutton(right_frame, text='Rueda', variable=self.ch9, width=20)
        ch_10 = tk.Checkbutton(right_frame, text='Rumba ', variable=self.ch10, width=20)
        ch_11 = tk.Checkbutton(right_frame, text='Female Style', variable=self.ch11, width=20)

        ch_1.grid(pady=10, row=0, column=0)
        ch_2.grid(pady=10, row=0, column=1)
        ch_3.grid(pady=10, row=0, column=2)
        ch_4.grid(pady=10, row=1, column=0)
        ch_5.grid(pady=10, row=1, column=1)
        ch_6.grid(pady=10, row=1, column=2)
        ch_7.grid(pady=10, row=2, column=0)
        ch_8.grid(pady=10, row=2, column=1)
        ch_9.grid(pady=10, row=2, column=2)
        ch_10.grid(pady=10, row=3, column=0)
        ch_11.grid(pady=10, row=3, column=1)


    def clear_info(self):
        self.name_info_entry.delete(0, tk.END)
        self.vk_entry.delete(0, tk.END)
        self.telephone_entry.delete(0, tk.END)
        self.birth_entry.delete(0, tk.END)
        self.root_entry.delete(0, tk.END)


    def add_student_info(self):
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("INSERT INTO students(name, vk_contact, telephone, birth, root, casino_new, casino_int, casino_adv,"
                  "bachata_new, bachata_int, ny_new, ny_int, ny_adv, rueda, rumba, female_style)" 
                  "VALUES(:name, :vk_contact, :telephone, :birth, :root, :casino_new, :casino_int, :casino_adv, "
                  ":bachata_new, :bachata_int, :ny_new, :ny_int, :ny_adv, :rueda, :rumba, :female_style)",
                  {
                      "name": self.name_info_entry.get(),
                      "vk_contact": self.vk_entry.get(),
                      "telephone": self.telephone_entry.get(),
                      "birth": self.birth_entry.get(),
                      "root": self.root_entry.get(),
                      "casino_new": self.ch1.get(),
                      "casino_int": self.ch2.get(),
                      "casino_adv": self.ch3.get(),
                      "ny_new": self.ch4.get(),
                      "ny_int": self.ch5.get(),
                      "ny_adv": self.ch6.get(),
                      "bachata_new": self.ch7.get(),
                      "bachata_int": self.ch8.get(),
                      "rueda": self.ch9.get(),
                      "rumba": self.ch10.get(),
                      "female_style": self.ch11.get(),
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
        self.name_label = tk.Label(main_frame, text='Дата', font=('Verdana', 25))
        self.name_label.grid(row=3, column=0, sticky=tk.NW, pady=12)

        self.name_entry = tk.Entry(main_frame, width=32, font=('Times New Roman', 20))
        self.name_entry.grid(row=0, column=1, padx=40, pady=12)
        self.type_entry = tk.Entry(main_frame, width=32, font=('Times New Roman', 20))
        self.type_entry.grid(row=1, column=1, padx=40, pady=12)
        self.cost_entry = tk.Entry(main_frame, width=32, font=('Times New Roman', 20))
        self.cost_entry.grid(row=2, column=1, padx=40, pady=12)
        self.date_entry = tk.Entry(main_frame, width=32, font=('Times New Roman', 20))
        self.date_entry.grid(row=3, column=1, padx=40, pady=12)

        #=========================   Info Frame   =======================

        info_frame = tk.Frame(self, width=800, height=500)
        info_frame.pack(side=tk.RIGHT)

        self.list_box = tk.Listbox(info_frame, width=600, height=300)
        self.list_box.pack()

    def clear_data(self):
            self.name_entry.delete(0, tk.END)
            self.type_entry.delete(0, tk.END)
            self.cost_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)

    def submit_data(self):
        # Add to Database
        conn = sqlite3.connect('mamboleo_adviser.db')
        c = conn.cursor()

        c.execute("INSERT INTO subscription VALUES(:date, :name, :lessons, :cost)",
                  {
                      "date": self.date_entry.get(),
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

        shedule_btn = tk.Button(manhattan_frame, width=17, text='Casino Adv // 18-30', command=self.open_casino_adv)
        shedule_btn.grid(row=0, column=1, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='NY Beg // 19-30', command=self.open_ny_new)
        shedule_btn.grid(row=0, column=2, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Rumba', command=self.open_rumba)
        shedule_btn.grid(row=0, column=3, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Bachata Int // 18-30', command=self.open_bachata_int)
        shedule_btn.grid(row=1, column=1, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Salsa Int // 19-30', command=self.open_casino_int)
        shedule_btn.grid(row=1, column=2, padx=15)
        shedule_btn= tk.Button(manhattan_frame, width=17, text='Bachata Beg // 20-30', command=self.open_bachta_new)
        shedule_btn.grid(row=1, column=3, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Casino Adv // 18-30', command=self.open_casino_adv)
        shedule_btn.grid(row=2, column=1, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='NY Beg // 19-30', command=self.open_ny_new)
        shedule_btn.grid(row=2, column=2, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Female Style', command=self.open_female_style)
        shedule_btn.grid(row=2, column=3, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Bachata Int // 18-30', command=self.open_bachata_int)
        shedule_btn.grid(row=3, column=1, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Salsa Int // 19-30', command=self.open_casino_int)
        shedule_btn.grid(row=3, column=2, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='Bachata Beg // 20-30', command=self.open_bachta_new)
        shedule_btn.grid(row=3, column=3, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='NY Int // 18-30', command=self.open_ny_int)
        shedule_btn.grid(row=4, column=1, padx=15)
        shedule_btn = tk.Button(manhattan_frame, width=17, text='NY Int // 18-30', command=self.open_ny_int)
        shedule_btn.grid(row=4, column=2, padx=15)


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

        shedule_btn = tk.Button(malecon_frame, width=17, text='Salsa Beg // 18-30', command=self.open_casino_new)
        shedule_btn.grid(row=0, column=1, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Bachata Int // 19-30', command=self.open_bachata_int)
        shedule_btn.grid(row=0, column=2, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Stretching // 20-30')
        shedule_btn.grid(row=0, column=3, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Salsa Beg // 18-30', command=self.open_casino_new)
        shedule_btn.grid(row=1, column=1, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='NY Adv // 19-30', command=self.open_ny_adv)
        shedule_btn.grid(row=1, column=2, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Salsa Beg // 18-30', command=self.open_casino_new)
        shedule_btn.grid(row=2, column=1, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Bachata Int // 19-30', command=self.open_bachata_int)
        shedule_btn.grid(row=2, column=2, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Stretching // 20-30')
        shedule_btn.grid(row=2, column=3, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Salsa Beg // 18-30', command=self.open_casino_new)
        shedule_btn.grid(row=3, column=1, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='NY Adv // 19-30', command=self.open_ny_adv)
        shedule_btn.grid(row=3, column=2, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Bachata Style // 18-00')
        shedule_btn.grid(row=4, column=1, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Rueda // 19-00', command=self.open_rueda)
        shedule_btn.grid(row=4, column=2, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Afro // 12-00')
        shedule_btn.grid(row=6, column=1, padx=15)
        shedule_btn = tk.Button(malecon_frame, width=17, text='Rueda // 13-00',command=self.open_rueda)
        shedule_btn.grid(row=6, column=2, padx=15)


    def open_casino_adv(self):
        casino_adv = Casino_Adv(self)
        casino_adv.grab_set()
        casino_adv.geometry('800x600')
        casino_adv.title('Casino Advanced 18-30')

    def open_ny_new(self):
        ny_new = NY_New(self)
        ny_new.grab_set()
        ny_new.geometry('800x600')
        ny_new.title('SalsaOn2 Begginers 19-30')

    def open_rumba(self):
        rumba = Rumba(self)
        rumba.grab_set()
        rumba.geometry('800x600')
        rumba.title('Rumba 20-30')

    def open_bachata_int(self):
        bachata_int = Bachata_Int(self)
        bachata_int.grab_set()
        bachata_int.geometry('800x600')
        bachata_int.title('Rumba 20-30')

    def open_casino_int(self):
        casino_int = Casino_Int(self)
        casino_int.grab_set()
        casino_int.geometry('800x600')
        casino_int.title('Casino Intermediate 19-30')

    def open_bachta_new(self):
        bachta_new = Bachata_New(self)
        bachta_new.grab_set()
        bachta_new.geometry('800x600')
        bachta_new.title('Bachata Begginers 20-30')

    def open_female_style(self):
        female_style = Female_Style(self)
        female_style.grab_set()
        female_style.geometry('800x600')
        female_style.title('Female Style 20-30')

    def open_ny_int(self):
        ny_int = NY_Int(self)
        ny_int.grab_set()
        ny_int.geometry('800x600')
        ny_int.title('SalsaOn2 Intermediate 20-30')

    def open_casino_new(self):
        win = Casino_New(self)
        win.grab_set()
        win.geometry('800x600')
        win.title('Casino Newcomer 20-30')

    def open_ny_adv(self):
        win = NY_Adv(self)
        win.grab_set()
        win.geometry('800x600')
        win.title('SalsaOn2 Advanced 19-30')

    def open_rueda(self):
        win = Rueda(self)
        win.grab_set()
        win.geometry('800x600')
        win.title('Rueda')

if __name__ == "__main__":
    root = Main()
    root.geometry('1300x680+0+0')

    root.mainloop()

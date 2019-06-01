from tkinter import *
import sqlite3

root = Tk()
root.geometry('800x600')

conn = sqlite3.connect('mamboleo_adviser.db')
c = conn.cursor()

c.execute("""CREATE TABLE students(
                    name PRIMARY KEY,
                    first_visit,
                    last_visit,
                    telephone,
                    vk_contact,
                    insta_contact,
                    lessons_visited,
                    root,
                    main_direction,
                    money_spent,
                    birth)""")

c.execute("""CREATE TABLE subscription(
                    date,
                    name TEXT,
                    lessons INT,
                    money INT,
                    FOREIGN KEY(name) REFERENCES students(name))""")



c.close()


from tkinter import *
import sqlite3

root = Tk()
root.geometry('800x600')

conn = sqlite3.connect('mamboleo_adviser.db')
c = conn.cursor()

c.execute("""CREATE TABLE casino_adv(
                    name text,
                    date,
                    FOREIGN KEY(name) REFERENCES students(name))""")




c.close()


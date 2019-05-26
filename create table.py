from tkinter import *
import sqlite3

root = Tk()
root.geometry('800x600')

conn = sqlite3.connect('subscription.db')
c = conn.cursor()

c.execute("""CREATE TABLE subscription(
                    date,
                    name TEXT,
                    lessons INT,
                    money INT)""")

c.close()

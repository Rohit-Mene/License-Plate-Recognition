from datetime import datetime
from tkinter import messagebox

import pymysql as pymysql

import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(50, 20, window=entry1)

entry2 = tk.Entry(root)
canvas1.create_window(50, 40, window=entry2)

entry3 = tk.Entry(root)
canvas1.create_window(50, 60, window=entry3)


def getSquareRoot():
    #x1 = entry1.get()

   # label1 = tk.Label(root, text=float(x1) ** 0.5)
   # canvas1.create_window(200, 230, window=label1)

    try:

        conn = pymysql.connect(host="127.0.0.1", user="root", passwd='root', db='smartpark')
        mycursor = conn.cursor()

        url = "select time_in from intimer where plate = 'Axpq4'"
        print(url)
        mycursor.execute(url)
        conn.commit()
        x=mycursor.fetchone()

        print(x)
        print("Successful")
        # msg(vehicle,mob,date,time,ty)
    except Exception as e:
        messagebox.showinfo(title="Error", message="Try Again")
        print(e)
    finally:
        conn.close()

button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)
canvas1.create_window(200, 180, window=button1)

root.mainloop()

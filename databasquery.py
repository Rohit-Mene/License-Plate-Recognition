from datetime import datetime
from tkinter import messagebox

import pymysql as pymysql


def save():
    licensep = "Axpq4"

    now = datetime.now()
    intime = now.strftime("%H:%M:%S")
    #intime = t2.get()
   # name = "Mene"
    #outtime = "4:00"



    try:

        conn = pymysql.connect(host="127.0.0.1", user="root", passwd='root', db='smartpark')
        mycursor = conn.cursor()

        url = "INSERT INTO intimer (plate,name_per,time_in,outtime) VALUES('"+licensep+"','"+name+"','"+intime+"','"+outtime+"')"
        print(url)
        mycursor.execute(url)
        conn.commit()
        print("Successful")
        #msg(vehicle,mob,date,time,ty)
    except Exception as e:
        messagebox.showinfo(title="Error", message="Try Again")
        print(e)
    finally:
        conn.close()

save()
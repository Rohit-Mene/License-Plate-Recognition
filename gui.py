from tkinter import *
#from recog import *
import recog

# create a tkinter window
root = Tk()

# Open window having dimension 100x100
root.geometry('100x100')

# Create a Button
btn = Button(root, text='Click me !', bd='5',
             command=recog.detectPlateRough )

# Set the position of button on the top of window.
btn.pack(side='top')

root.mainloop()
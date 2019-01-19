import tkinter
from tkinter import messagebox
from tkinter import *
from random import *
from Player import *

height_f, width_f, cellsize = [16, 12, 64]

root = Tk()
canvas = Canvas(root, width = cellsize * height_f + cellsize * 2, height = cellsize * width_f)

#canvas.create_rectangle(0, 0, cellsize * height_f, cellsize * width_f, fill = 'red')

#здесь скоро будут бинды

canvas.pack()
root.mainloop()
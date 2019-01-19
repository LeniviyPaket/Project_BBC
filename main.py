import os
import tkinter
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from random import *

#importing some mechanics
from Player import *
from Enemy import *
from Tile import *
from Weapon import *

height_f, width_f, cellsize = [16, 12, 64]

#height_f, width_f, cellsize = [3, 3, 64]

field = []
with open("polygon.txt", "r") as f:
    for line in f:
        field.append(list(line.strip()))


root = tkinter.Tk()
#canvas = Canvas(root, width = cellsize * height_f, height = cellsize * width_f)

#root.columnconfigure(0, pad = cellsize)
#root.columnconfigure(1, pad = cellsize)
#root.columnconfigure(2, pad = cellsize)
#root.columnconfigure(3, pad = cellsize)
#root.columnconfigure(4, pad = cellsize)

#root.rowconfigure(0, pad = cellsize)
#root.rowconfigure(1, pad = cellsize)
#root.rowconfigure(2, pad = cellsize)
#root.rowconfigure(3, pad = cellsize)
#root.rowconfigure(4, pad = cellsize)

print(*field)

imgwall = ImageTk.PhotoImage(Image.open('/home/svs/Desktop/Gamehack_2019/sprites/floor_3.png'))
imgfloor = ImageTk.PhotoImage(Image.open('/home/svs/Desktop/Gamehack_2019/sprites/g_floor_base.png'))

for j in range(height_f):
    for i in range(width_f):
        if field[i][j] == '#':
            tkinter.Label(root, image=imgwall).grid(column = j, row = i)
        elif field[i][j] == '.':
            tkinter.Label(root, image=imgfloor).grid(column = j, row = i)

#canvas.create_rectangle(0, 0, cellsize * height_f, cellsize * width_f, fill = 'red')

##здесь скоро будут бинды

#canvas.pack()
root.mainloop()
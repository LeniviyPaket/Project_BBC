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


field = []
with open("polygon.txt", "r") as f:
    for line in f:
        field.append(list(line))


root = tkinter.Tk()
canvas = tkinter.Canvas(root, width = cellsize * height_f, height = cellsize * width_f)

for i in range(width_f):
    for j in range(height_f):
        if field[i][j] == '#':
            img = ImageTk.PhotoImage(Image.open(os.getcwd() + '/sprites/g_wall_base.png'))
            tkinter.Label(root, image=img).pack()
        else:
            img = ImageTk.PhotoImage(Image.open(os.getcwd() + '/sprites/g_floor_base.png'))
            tkinter.Label(root, image=img).pack()
            

#canvas.create_rectangle(0, 0, cellsize * height_f, cellsize * width_f, fill = 'red')

##здесь скоро будут бинды

#img = ImageTk.PhotoImage(Image.open(os.getcwd() + '/sprites/hl_weapon.png'))
#view = tkinter.Label(root, padx = 100, pady = 100, image=img)
#view.pack()
#view.pack(side="center", fill="both", expand="yes")
canvas.pack()
root.mainloop()
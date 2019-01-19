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
#print(*field)

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
##а сейчас здесь только танцы с бубном

root.mainloop()
import os
import tkinter
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from random import *

#importing some mechanics
import Player
import Enemy
import Tile
import Weapon

height_f, width_f, cellsize = [16, 12, 64]

#height_f, width_f, cellsize = [3, 3, 64]

field = []
with open("polygon.txt", "r") as f:
    for line in f:
        field.append(list(line.strip()))

Jacket = Player.player()
Jacket.x, Jacket.y = height_f * cellsize // 2, width_f * cellsize // 2

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width = cellsize * height_f, height = cellsize * width_f)
#print(*field)

Jacketsprite = ImageTk.PhotoImage(Image.open(os.getcwd() + '/sprites/enemy_0_1.png'))
imgwall = ImageTk.PhotoImage(Image.open(os.getcwd() + '/sprites/floor_3.png'))
imgfloor = ImageTk.PhotoImage(Image.open(os.getcwd() + '/sprites/g_floor_base.png'))

for j in range(height_f):
    for i in range(width_f):
        if field[i][j] == '#':
            canvas.create_image(j * cellsize, i * cellsize, anchor = "nw", image=imgwall)
        elif field[i][j] == '.':
            canvas.create_image(j * cellsize, i * cellsize, anchor = "nw", image=imgfloor)

canvas.create_image(Jacket.x, Jacket.y, image=Jacketsprite)

##здесь скоро будут бинды
##а сейчас здесь только танцы с бубном

canvas.pack()
root.mainloop()
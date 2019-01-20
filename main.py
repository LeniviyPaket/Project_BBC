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

#тут читаем поле
field = []
with open("polygon.txt", "r") as f:
    for line in f:
        field.append(list(line.strip()))

#а тут задаем параметры ГГ (кодовое имя --- Курточка)
Jacket = Player.player()
Jacket.x, Jacket.y = height_f * cellsize // 2, width_f * cellsize // 2
Jacket.speed = cellsize // 2
Jacket.sprite = os.getcwd() + '/sprites/enemy_0_1.png'


#пилим окно
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width = cellsize * height_f, height = cellsize * width_f)

#создаем спрайты
Jacketsprite = ImageTk.PhotoImage(Image.open(Jacket.sprite))
imgwall = ImageTk.PhotoImage(Image.open(os.getcwd() + '/sprites/floor_3.png'))
imgfloor = ImageTk.PhotoImage(Image.open(os.getcwd() + '/sprites/g_floor_base.png'))


#генерируем текстуры поля
for j in range(height_f):
    for i in range(width_f):
        if field[i][j] == '#':
            canvas.create_image(j * cellsize, i * cellsize, anchor = "nw", image=imgwall)
        elif field[i][j] == '.':
            canvas.create_image(j * cellsize, i * cellsize, anchor = "nw", image=imgfloor)

#создаем тело персонажа
charbody = canvas.create_image(Jacket.x, Jacket.y, image=Jacketsprite)


##здесь скоро будут бинды
##а сейчас здесь только танцы с бубном

#       []  <--- бубен
#     O/
#    /V
#     |
#    / \
# {танцует}

#а вот и бинды
#warning: из-за того, что я ниоч понимаю принцип работы ткинтера, все будет костыльно

def charmoveup():
    canvas.delete(charbody)
    Jacket.moveup()
    charbody = canvas.create_image(Jacket.x, Jacket.y, image=Jacketsprite)
    canvas.update()

canvas.bind("<Up>", charmoveup)
#canvas.bind("a", charmoveleft)
#canvas.bind("s", charmovedown)
#canvas.bind("d", charmoveright)

canvas.pack()
root.mainloop()
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
imgfloor = ImageTk.PhotoImage(Image.open(os.getcwd() + '/sprites/floor3.png'))


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

def char_move_left():
    global charbody
    #Jacket.move_up()
    canvas.move(charbody, -1 * Jacket.speed, 0)
    canvas.update()

def char_move_down():
    global charbody
    #Jacket.move_up()
    canvas.move(charbody, 0, Jacket.speed)
    canvas.update()

def char_move_right():
    global charbody
    #Jacket.move_up()
    canvas.move(charbody, Jacket.speed, 0)
    canvas.update()

def char_move_up():
    global charbody
    #Jacket.move_up()
    canvas.move(charbody, 0, -1 * Jacket.speed)
    canvas.update()


#рандомный кувырок. все как вы любите --- сплошные костыли
def char_random_dodge():
    for _ in range(2):
        act = randint(0, 3)
        if act == 0:
            char_move_up()
        elif act == 1:
            char_move_down()
        elif act == 2:
            char_move_left()
        elif act == 3:
            char_move_right()

#тут отзываемся на нажатия клавиш
def callback(event):
    if event.char == "w":
        char_move_up()
    if event.char == "a":
        char_move_left()
    if event.char == "s":
        char_move_down()
    if event.char == "d":
        char_move_right()
    if event.char == "f":
        char_random_dodge()

root.bind("<Key>", callback)

canvas.pack()
root.mainloop()
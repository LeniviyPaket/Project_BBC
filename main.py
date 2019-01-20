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
from entity import *

main_field = Main_field()
main_field.add_entity('player')
main_field.get_list_ent()

height_f, width_f, cellsize = [16, 12, 64]
dodge_dist = cellsize

#height_f, width_f, cellsize = [3, 3, 64]

#тут читаем поле
field = []
with open("polygon.txt", "r") as f:
    for line in f:
        field.append(list(line.strip()))



#а тут задаем параметры ГГ (кодовое имя --- Курточка)
Jacket = Player.player()
Jacket.x, Jacket.y = height_f * cellsize // 2, width_f * cellsize // 2
Jacket.speed = main_field.get_list_ent()[0][0].max_move_speed
Jacket.sprite = os.getcwd() + '/sprites/enemy_0_1.png'


#пилим окно
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width = cellsize * height_f, height = cellsize * width_f)

#создаем спрайты
Jacketsprite = ImageTk.PhotoImage(Image.open(Jacket.sprite))
imgwall = ImageTk.PhotoImage(Image.open(os.getcwd() + '/sprites/wall1.png'))
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

def char_move_left(x):
    global charbody
    main_field.move_left(0)
    #Jacket.move_up()
    canvas.move(charbody, -1 * x, 0)
    canvas.update()

def char_move_down(x):
    global charbody
    main_field.move_down(0)
    #Jacket.move_up()
    canvas.move(charbody, 0, x)
    canvas.update()

def char_move_right(x):
    global charbody
    main_field.move_right(0)
    #Jacket.move_up()
    canvas.move(charbody, x, 0)
    canvas.update()

def char_move_up(x):
    global charbody
    main_field.move_up(0)
    #Jacket.move_up()
    canvas.move(charbody, 0, -1 * x)
    canvas.update()


#рандомный кувырок. все как вы любите --- сплошные костыли
def char_random_dodge():
    for _ in range(2):
        act = randint(0, 3)
        if act == 0:
            char_move_up(dodge_dist)
        elif act == 1:
            char_move_down(dodge_dist)
        elif act == 2:
            char_move_left(dodge_dist)
        elif act == 3:
            char_move_right(dodge_dist)


def char_attack():
    pass


#тут отзываемся на нажатия клавиш
def callback(event):
    if event.char == "w":
        char_move_up(Jacket.speed)
    if event.char == "a":
        char_move_left(Jacket.speed)
    if event.char == "s":
        char_move_down(Jacket.speed)
    if event.char == "d":
        char_move_right(Jacket.speed)
    if event.char == "f":
        char_random_dodge()
    if event.char == " ":
        char_attack()

root.bind("<Key>", callback)

canvas.pack()
root.mainloop()
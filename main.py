import os
import tkinter
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from random import *
from copy import deepcopy


#importing some mechanics
import Player
import Enemy
import Tile
import Weapon
from entity import *

main_field = Main_field()

#создаем "список живых существ"
entities_alive = {}

height_f, width_f, cellsize = [16, 12, 64]
dodge_dist = cellsize

#height_f, width_f, cellsize = [3, 3, 64]

#тут читаем поле
field = []
with open("polygon.txt", "r") as f:
    for line in f:
        field.append(list(line.strip()))


entities_to_obj = {}


#а тут задаем параметры ГГ (кодовое имя --- Курточка)
main_field.add_entity('player',entity_id='player',entity_pos = [cellsize*4,cellsize*4])
entities_alive['player'] = "player"
Jacket = Player.player()
Jacket.x, Jacket.y = main_field.get_list_ent()[0][1][0] + cellsize, main_field.get_list_ent()[0][1][1] + cellsize
Jacket.speed = main_field.get_list_ent()[0][0].max_move_speed
Jacket.sprite = os.getcwd() + '/sprites/enemy_0_1.png'

#задаем манекен
main_field.add_entity('enemy',entity_id='enemy_1')
entities_alive['enemy_1'] = "enemy_1"
Man = Player.player()
Man.x, Man.y = main_field.get_list_ent()[1][1][0] + cellsize, main_field.get_list_ent()[1][1][1] + cellsize
Man.speed = main_field.get_list_ent()[0][0].max_move_speed
Man.sprite = os.getcwd() + '/sprites/weapon.png'

#пилим окно
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width = cellsize * height_f, height = cellsize * width_f)

#создаем спрайты
Jacketsprite = ImageTk.PhotoImage(Image.open(Jacket.sprite))
Mansprite = ImageTk.PhotoImage(Image.open(Man.sprite))
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
entities_to_obj['player'] = canvas.create_image(Jacket.x, Jacket.y, image=Jacketsprite)

#создаем манекен
entities_to_obj['enemy_1'] = canvas.create_image(Man.x, Man.y, image=Mansprite)


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
    global entities_to_obj
    old_pos = deepcopy(main_field.get_list_ent()[0][1])
    main_field.move_left(0)
    new_pos = main_field.get_list_ent()[0][1]
    #Jacket.move_up()
    canvas.move(entities_to_obj['player'], new_pos[0]-old_pos[0], new_pos[1]-old_pos[1])
    canvas.update()

def char_move_down(x):
    global entities_to_obj
    old_pos = deepcopy(main_field.get_list_ent()[0][1])
    main_field.move_down(0)
    new_pos = main_field.get_list_ent()[0][1]
    #Jacket.move_up()
    canvas.move(entities_to_obj['player'], new_pos[0]-old_pos[0], new_pos[1]-old_pos[1])
    canvas.update()

def char_move_right(x):
    global entities_to_obj
    old_pos = deepcopy(main_field.get_list_ent()[0][1])
    main_field.move_right(0)
    new_pos = main_field.get_list_ent()[0][1]
    #Jacket.move_up()
    canvas.move(entities_to_obj['player'], new_pos[0]-old_pos[0], new_pos[1]-old_pos[1])
    canvas.update()

def char_move_up(x):
    global entities_to_obj
    old_pos = deepcopy(main_field.get_list_ent()[0][1])
    main_field.move_up(0)
    new_pos = main_field.get_list_ent()[0][1]
    #Jacket.move_up()
    canvas.move(entities_to_obj['player'], new_pos[0]-old_pos[0], new_pos[1]-old_pos[1])
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
    died_list = main_field.atack(0)
    #print(died_list)
    if died_list is not None:
        for dead in died_list:
            canvas.delete(entities_to_obj[dead])



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
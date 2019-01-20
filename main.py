import os
import tkinter
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from random import *
from copy import deepcopy
import time


#importing some mechanics
import Player
import Enemy
import Tile
import Weapon
from entity import *

#подключаем музычку, но позже

main_field = Main_field()
count_of_moves = 0
dead = []

#создаем "список живых существ"

height_f, width_f, cellsize = [16, 12, 64]
dodge_dist = cellsize

#height_f, width_f, cellsize = [3, 3, 64]

#тут читаем поле
field = []
with open("polygon.txt", "r") as f:
    for line in f:
        field.append(list(line.strip()))

entity_id_to_id = {}


entities_to_obj = {}


#а тут задаем параметры ГГ (кодовое имя --- Курточка)
main_field.add_entity('player',entity_id='player',entity_pos = [cellsize*4,cellsize*4])
entity_id_to_id['player'] = 0
Jacket = Player.player()
Jacket.x, Jacket.y = main_field.get_list_ent()[0][1][0] + cellsize * 3 // 2, main_field.get_list_ent()[0][1][1] + cellsize * 3 // 2
Jacket.speed = main_field.get_list_ent()[0][0].max_move_speed
Jacket.sprite = os.getcwd() + '/sprites/player.png'

#пилим окно
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width = cellsize * height_f, height = cellsize * width_f)

#создаем спрайты
Jacketsprite = ImageTk.PhotoImage(Image.open(Jacket.sprite))
Mansprite = ImageTk.PhotoImage(Image.open(os.getcwd() + '/sprites/enemy_very_pink.png'))
Attacksprite = ImageTk.PhotoImage(Image.open(os.getcwd() + '/sprites/atack.png'))
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

def create_enemy(pos = [1024//2,768//2]):
    global entity_id_to_id
    global entities_to_obj
    global canvas
    global Mansprite
    enemy_name = 'enemy_'+str(len(main_field.get_list_ent()))
    main_field.add_entity('enemy',entity_id=enemy_name,entity_pos=pos)
    entity_id_to_id[enemy_name] = 1
    Man = Player.player()
    Man.x, Man.y = main_field.get_list_ent()[len(main_field.get_list_ent())-1][1][0] + cellsize * 3 // 2, main_field.get_list_ent()[len(main_field.get_list_ent())-1][1][1] + cellsize * 3 // 2
    Man.speed = main_field.get_list_ent()[0][0].max_move_speed
    entities_to_obj[enemy_name] = canvas.create_image(Man.x, Man.y, image=Mansprite)
create_enemy()




















##                                                              здесь скоро будут бинды
##                                                              а сейчас здесь только танцы с бубном

#                                                                      (c)  <--- бубен
#                                                                    O/
#                                                                   /V
#                                                                    |
#                                                                   / \
#                                                                *танцует*

#                                                               а вот и бинды














#warning: из-за того, что я ниоч понимаю принцип работы ткинтера, все будет костыльно

def char_move_left(x, whom):
    global entities_to_obj
    old_pos = deepcopy(main_field.get_list_ent()[entity_id_to_id[whom]][1])
    main_field.move_left(entity_id_to_id[whom])
    new_pos = main_field.get_list_ent()[entity_id_to_id[whom]][1]
    #Jacket.move_up()
    canvas.move(entities_to_obj[whom], new_pos[0]-old_pos[0], new_pos[1]-old_pos[1])
    canvas.update()

def char_move_down(x, whom):
    global entities_to_obj
    old_pos = deepcopy(main_field.get_list_ent()[entity_id_to_id[whom]][1])
    main_field.move_down(entity_id_to_id[whom])
    new_pos = main_field.get_list_ent()[entity_id_to_id[whom]][1]
    #Jacket.move_up()
    canvas.move(entities_to_obj[whom], new_pos[0]-old_pos[0], new_pos[1]-old_pos[1])
    canvas.update()

def char_move_right(x, whom):
    global entities_to_obj
    old_pos = deepcopy(main_field.get_list_ent()[entity_id_to_id[whom]][1])
    main_field.move_right(entity_id_to_id[whom])
    new_pos = main_field.get_list_ent()[entity_id_to_id[whom]][1]
    #Jacket.move_up()
    canvas.move(entities_to_obj[whom], new_pos[0]-old_pos[0], new_pos[1]-old_pos[1])
    canvas.update()

def char_move_up(x, whom):
    global entities_to_obj
    old_pos = deepcopy(main_field.get_list_ent()[entity_id_to_id[whom]][1])
    main_field.move_up(entity_id_to_id[whom])
    new_pos = main_field.get_list_ent()[entity_id_to_id[whom]][1]
    #Jacket.move_up()
    canvas.move(entities_to_obj[whom], new_pos[0]-old_pos[0], new_pos[1]-old_pos[1])
    canvas.update()


#рандомный кувырок. все как вы любите --- сплошные костыли
def char_random_dodge(whom, x):
    for _ in range(x):
        act = randint(0, 3)
        if act == 0:
            char_move_up(dodge_dist, whom)
        elif act == 1:
            char_move_down(dodge_dist, whom)
        elif act == 2:
            char_move_left(dodge_dist, whom)
        elif act == 3:
            char_move_right(dodge_dist, whom)

killed = []
score = 0
txt = canvas.create_text((height_f - 2) * cellsize, cellsize // 2, text = "Score: " + str(score), font = "Verdana 24", justify = tkinter.CENTER, fill = "black")

#атака
def char_attack(whom):
    global killed
    global score, txt
    old_pos = (main_field.get_list_ent()[entity_id_to_id[whom]][1][0] + cellsize * 3 // 2, main_field.get_list_ent()[entity_id_to_id[whom]][1][1] + cellsize * 3 // 2)
    r = main_field.get_list_ent()[0][0].atack_range
    atck_gui = canvas.create_image(old_pos[0], old_pos[1], image=Attacksprite)
    if whom == 'player':
        sprite = Jacketsprite
    else:
        sprite = Mansprite
    char_copy = canvas.create_image(old_pos[0], old_pos[1], image=sprite)
    died_list = main_field.atack(entity_id_to_id[whom])
    canvas.update()
    #print(died_list)
    time.sleep(0.125)
    canvas.delete(atck_gui)
    canvas.delete(char_copy)
    if died_list is not None:
        for dead in died_list:
            canvas.delete(entities_to_obj[dead])
            killed.append(dead)
            if 'player' in died_list:
                #endpic = ImageTk.PhotoImage(Image.open(os.getcwd() + '/sprites/gameover.png'))
                #canvas.create_image(0, 0, image=endpic)

                messagebox.showinfo('', 'You died')
                root.withdraw()
                for _ in range(200):
                    print("YOU DIED")
                exit()
            score += 1
            canvas.delete(txt)
            txt = canvas.create_text((height_f - 2) * cellsize, cellsize // 2, text = "Score: " + str(score), font = "Verdana 24", justify = tkinter.CENTER, fill = "black")



#тут отзываемся на нажатия клавиш
def callback(event):
    global count_of_moves
    global killed
    dead = killed
    if event.char == "w":
        char_move_up(Jacket.speed, 'player')
        time.sleep(0.0625)
        list_of_ent = main_field.get_list_ent()
        for key in entity_id_to_id.keys():
            if entity_id_to_id[key] != 0 and (key not in dead):
                result = list_of_ent[entity_id_to_id[key]][0].move_to_player(list_of_ent[0][1],list_of_ent[0][0].hit_box_range,list_of_ent[entity_id_to_id[key]][1])
                if result == 'up':
                    char_move_up(None,key)
                if result == 'down':
                    char_move_down(None,key)
                if result == 'left':
                    char_move_left(None,key)
                if result == 'right':
                    char_move_right(None,key)
                if result == 'atack':
                    char_attack(key)                

    if event.char == "a":
        char_move_left(Jacket.speed, 'player')
        time.sleep(0.0625)
        list_of_ent = main_field.get_list_ent()
        for key in entity_id_to_id.keys():
            if entity_id_to_id[key] != 0 and (key not in dead):
                result = list_of_ent[entity_id_to_id[key]][0].move_to_player(list_of_ent[0][1],list_of_ent[0][0].hit_box_range,list_of_ent[entity_id_to_id[key]][1])
                if result == 'up':
                    char_move_up(None,key)
                if result == 'down':
                    char_move_down(None,key)
                if result == 'left':
                    char_move_left(None,key)
                if result == 'right':
                    char_move_right(None,key)
                if result == 'atack':
                    char_attack(key)
    if event.char == "s":
        char_move_down(Jacket.speed, 'player')
        time.sleep(0.0625)
        list_of_ent = main_field.get_list_ent()
        for key in entity_id_to_id.keys():
            if entity_id_to_id[key] != 0 and (key not in dead):
                result = list_of_ent[entity_id_to_id[key]][0].move_to_player(list_of_ent[0][1],list_of_ent[0][0].hit_box_range,list_of_ent[entity_id_to_id[key]][1])
                if result == 'up':
                    char_move_up(None,key)
                if result == 'down':
                    char_move_down(None,key)
                if result == 'left':
                    char_move_left(None,key)
                if result == 'right':
                    char_move_right(None,key)
                if result == 'atack':
                    char_attack(key)
    if event.char == "d":
        char_move_right(Jacket.speed, 'player')
        time.sleep(0.0625)
        list_of_ent = main_field.get_list_ent()
        for key in entity_id_to_id.keys():
            if entity_id_to_id[key] != 0 and (key not in dead):
                result = list_of_ent[entity_id_to_id[key]][0].move_to_player(list_of_ent[0][1],list_of_ent[0][0].hit_box_range,list_of_ent[entity_id_to_id[key]][1])
                if result == 'up':
                    char_move_up(None,key)
                if result == 'down':
                    char_move_down(None,key)
                if result == 'left':
                    char_move_left(None,key)
                if result == 'right':
                    char_move_right(None,key)
                if result == 'atack':
                    char_attack(key)
    if event.char == "f":
        char_random_dodge('player', 2)
        list_of_ent = main_field.get_list_ent()
        for key in entity_id_to_id.keys():
            if entity_id_to_id[key] != 0 and (key not in dead):
                result = list_of_ent[entity_id_to_id[key]][0].move_to_player(list_of_ent[0][1],list_of_ent[0][0].hit_box_range,list_of_ent[entity_id_to_id[key]][1])
                if result == 'up':
                    char_move_up(None,key)
                if result == 'down':
                    char_move_down(None,key)
                if result == 'left':
                    char_move_left(None,key)
                if result == 'right':
                    char_move_right(None,key)
                if result == 'atack':
                    char_attack(key)
    if event.char == " ":
        char_attack('player')
        list_of_ent = main_field.get_list_ent()
        for key in entity_id_to_id.keys():
            if entity_id_to_id[key] != 0 and (key not in dead):
                result = list_of_ent[entity_id_to_id[key]][0].move_to_player(list_of_ent[0][1],list_of_ent[0][0].hit_box_range,list_of_ent[entity_id_to_id[key]][1])
                if result == 'up':
                    char_move_up(None,key)
                if result == 'down':
                    char_move_down(None,key)
                if result == 'left':
                    char_move_left(None,key)
                if result == 'right':
                    char_move_right(None,key)
                if result == 'atack':
                    char_attack(key)
    name = [' ','f','w','s','a','d']
    if event.char in name:
        if count_of_moves//10 < (count_of_moves+1)//10:
            create_enemy()
            count_of_moves+=1
        else:
            count_of_moves+=1



root.bind("<Key>", callback)

canvas.pack()
root.mainloop()

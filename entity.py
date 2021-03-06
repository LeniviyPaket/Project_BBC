from copy import deepcopy

class entity(object):
    def __init__(self,weapon=1,max_helth=10,max_move_speed=32,atack_range=64,hit_box_range=5):
        self.weapon = weapon
        self.curent_helth = max_helth
        self.max_move_speed = max_move_speed
        self.hit_box_range = hit_box_range
    def hited(self,damage=0):
        self.curent_helth -=damage
        if self.curent_helth <= 0:
            return True
        return False


class WeaponP():
    def __init__(self,damage=5,atack_range=120):
        self.damage=damage
        self.atack_range = atack_range
class WeaponE():
    def __init__(self,damage=1,atack_range=65):
        self.damage=damage
        self.atack_range = atack_range

class Player_c():
    def __init__(self,weapon=WeaponP(),max_helth=10,max_move_speed=32,hit_box_range=32,enemy_id=None):
        self.enemy_id = enemy_id
        self.damage = weapon.damage
        self.curent_helth = max_helth
        self.max_move_speed = max_move_speed
        self.hit_box_range = hit_box_range
        self.atack_range = weapon.atack_range
    def hited(self,damage=0):
        self.curent_helth -=damage
        if self.curent_helth <= 0:
            return True
        return False
    def update_weapon(self,weapon):
        self.damage = weapon.damage
        self.atack_range = weapon.atack_range

class Enemy():
    def __init__(self,weapon=WeaponE(),max_helth=10,max_move_speed=32,hit_box_range=32, enemy_id = None):
        self.enemy_id = enemy_id
        self.damage = weapon.damage
        self.curent_helth = max_helth
        self.max_move_speed = max_move_speed
        self.hit_box_range = hit_box_range
        self.atack_range = weapon.atack_range
    def hited(self,damage=0):
        self.curent_helth -=damage
        if self.curent_helth <= 0:
            return True
        return False
    def move_to_player(self,player_pos,player_hit_box_range,self_pos):
        base_dist = calc_dist(player_pos,self_pos)
        if base_dist<player_hit_box_range+self.atack_range:
            return "atack"
        pos_moves = ['up','left','right','down']
        if base_dist>calc_dist(player_pos,[self_pos[0],self_pos[1]-self.max_move_speed]):
            return pos_moves[0]
        if base_dist>calc_dist(player_pos,[self_pos[0]-self.max_move_speed,self_pos[1]]):
            return pos_moves[1]
        if base_dist>calc_dist(player_pos,[self_pos[0]+self.max_move_speed,self_pos[1]]):
            return pos_moves[2]
        if base_dist>calc_dist(player_pos,[self_pos[0],self_pos[1]+self.max_move_speed]):
            return pos_moves[3]
entity_dict = {
    'enemy'  : Enemy,
    'player' : Player_c
}

class Main_field(object):
    def __init__(self,field_size=(1024-192,768-192)):
        self.field_x = field_size[0]
        self.field_y = field_size[1]
        self.entity_list = []



    #получит расположение всех обьектов на доске
    def get_list_ent(self):
        return self.entity_list

    #добавить entity на доску 
    def add_entity(self,entity_type,entity_id=None,entity_pos = None):
        if entity_pos is None:
            entity_pos = [self.field_x//2,self.field_y//2]
        self.entity_list.append((entity_dict[entity_type](enemy_id=entity_id),entity_pos))


	#передвинуть entity на шаг в соответсвующем направлении
    def move_up(self,entity_id):
        old_pos = deepcopy(self.entity_list[entity_id][1])
        self.entity_list[entity_id][1][1] = max(self.entity_list[entity_id][1][1] - self.entity_list[entity_id][0].max_move_speed,0)
        entity = self.entity_list[entity_id]
        for enemy in self.entity_list:
            if enemy != entity:
                if (calc_dist(entity[1],enemy[1])<(entity[0].hit_box_range+enemy[0].hit_box_range)):
                    self.entity_list[entity_id][1][1]=old_pos[1]

    def move_down(self,entity_id):
        old_pos = deepcopy(self.entity_list[entity_id][1])
        self.entity_list[entity_id][1][1] = min(self.entity_list[entity_id][1][1] + self.entity_list[entity_id][0].max_move_speed,self.field_y)
        entity = self.entity_list[entity_id]
        for enemy in self.entity_list:
            if enemy != entity:
                if (calc_dist(entity[1],enemy[1])<(entity[0].hit_box_range+enemy[0].hit_box_range)):
                    self.entity_list[entity_id][1][1]=old_pos[1]
    def move_left(self,entity_id):
        old_pos = deepcopy(self.entity_list[entity_id][1])
        self.entity_list[entity_id][1][0] = max(self.entity_list[entity_id][1][0] - self.entity_list[entity_id][0].max_move_speed,0)
        entity = self.entity_list[entity_id]
        for enemy in self.entity_list:
            if enemy != entity:
                if (calc_dist(entity[1],enemy[1])<(entity[0].hit_box_range+enemy[0].hit_box_range)):
                    self.entity_list[entity_id][1][0]=old_pos[0]
    def move_right(self,entity_id):
        old_pos = deepcopy(self.entity_list[entity_id][1])
        self.entity_list[entity_id][1][0] = min(self.entity_list[entity_id][1][0] + self.entity_list[entity_id][0].max_move_speed,self.field_x)
        entity = self.entity_list[entity_id]
        for enemy in self.entity_list:
            if enemy != entity:
                if (calc_dist(entity[1],enemy[1])<(entity[0].hit_box_range+enemy[0].hit_box_range)):
                    self.entity_list[entity_id][1][0]=old_pos[0]


    def atack(self,entity_id):
        entity = self.entity_list[entity_id]
        to_remove = []
        kicked = []
        for enemy in self.entity_list:
            if enemy != entity:
                if (calc_dist(entity[1],enemy[1])<(entity[0].atack_range+enemy[0].hit_box_range)):
                    kicked.append(enemy)
                    if enemy[0].hited(entity[0].damage):
                        to_remove.append(enemy)
        for i in to_remove:
            self.entity_list.remove(i)
        a = [i[0].enemy_id for i in to_remove]
        #print(a)
        return a


def calc_dist(pos_1,pos_2):
    return ((pos_1[0]-pos_2[0])**2 + (pos_1[1]-pos_2[1])**2)**0.5

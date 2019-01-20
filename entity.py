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




class Player_c():
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
class Enemy(entity):
    def __init__(self):
        super().__init__()


entity_dict = {
    'enemy'  : Enemy,
    'player' : Player_c
}

class Main_field(object):
    def __init__(self,field_size=(1024-128,768-128)):
        self.field_x = field_size[0]
        self.field_y = field_size[1]
        self.entity_list = []



    #получит расположение всех обьектов на доске
    def get_list_ent(self):
        return self.entity_list

    #добавить entity на доску 
    def add_entity(self,entity_type,entity_pos = None):
        if entity_pos is None:
            entity_pos = [self.field_x//2,self.field_y//2]
        self.entity_list.append((entity_dict[entity_type](),entity_pos))


	#передвинуть entity на шаг в соответсвующем направлении
    def move_up(self,entity_id):
        self.entity_list[entity_id][1][1] -= self.entity_list[entity_id][0].max_move_speed
    def move_down(self,entity_id):
        self.entity_list[entity_id][1][1] += self.entity_list[entity_id][0].max_move_speed
    def move_left(self,entity_id):
        self.entity_list[entity_id][1][0] -= self.entity_list[entity_id][0].max_move_speed
    def move_right(self,entity_id):
        self.entity_list[entity_id][1][0] += self.entity_list[entity_id][0].max_move_speed


    def atack_up(self,entity_id):
        entity = self.entity_list[entity_id]
        to_remove = []
        for enemy in self.entity_list:
            if num != entity_id:
                if (calc_dist(entity[1],enemy[1])<(entity[0].atack_range+enemy[0].hit_box_range)) and (enemy[1][0]>entity[1][0]):
                    if enemy[0].hited(entity[0].weapon):
                        to_remove.append(enemy)
        for i in to_remove:
            self.entity_list.remove(i)
    def atack_down(self,entity_id):
        entity = self.entity_list[entity_id]
        to_remove = []
        for enemy in self.entity_list:
            if num != entity_id:
                if (calc_dist(entity[1],enemy[1])<(entity[0].atack_range+enemy[0].hit_box_range)) and (enemy[1][0]<entity[1][0]):
                    if enemy[0].hited(entity[0].weapon):
                        to_remove.append(enemy)
        for i in to_remove:
            self.entity_list.remove(i)
    def atack_left(self,entity_id):
        entity = self.entity_list[entity_id]
        to_remove = []
        for enemy in self.entity_list:
            if num != entity_id:
                if (calc_dist(entity[1],enemy[1])<(entity[0].atack_range+enemy[0].hit_box_range)) and (enemy[1][1]<entity[1][1]):
                    if enemy[0].hited(entity[0].weapon):
                        to_remove.append(enemy)
        for i in to_remove:
            self.entity_list.remove(i)
    def atack_right(self,entity_id):
        entity = self.entity_list[entity_id]
        to_remove = []
        for enemy in self.entity_list:
            if num != entity_id:
                if (calc_dist(entity[1],enemy[1])<(entity[0].atack_range+enemy[0].hit_box_range)) and (enemy[1][1]>entity[1][1]):
                    if enemy[0].hited(entity[0].weapon):
                        to_remove.append(enemy)
        for i in to_remove:
            self.entity_list.remove(i)

def calc_dist(pos_1,pos_2):
    return ((pos_1[0]-pos_2[1])**2 + (pos_1[1]-pos_2[1])**2)**0.5

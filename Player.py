class player():
    #some variables
    
    #vars for drawing
    x = None
    y = None
    ang = None
    
    #stats
    hpmax = None
    hpcurrent = None
    speed = None

    #equipment
    weapon = None
    qslot1 = None
    qslot2 = None
    inventory = []


    #movement
    def moveup():
        y += speed
    def movedown():
        y -= speed
    def moveleft():
        x -= speed
    def moveright():
        x += speed


    #dodging
    def dodgeup():
        pass
    def dodgedown():
        pass
    def dodgeright():
        pass
    def dodgeleft():
        pass
    def randomdodge():
        pass


    #attacking enemies
    def aim():
        pass
    def shoot():
        pass
    def useitem():
        pass


    #some interactive things
    def pickweapon():
        pass
    def dropweapon():
        pass
    def pickitem():
        pass
    def dropitem():
        pass
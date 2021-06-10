def norm(x, y):
    return (x**2 + y**2)**0.5

def distance(x1, y1, x2, y2):
    deltaX = x2-x1
    deltaY = y2-y1
    return norm(deltaX, deltaY)

Center = (23, 37)
CenterFactor = 5
def awayFromWalls(x, y):
    d = distance(x, y, Center[0], Center[1])
    F = CenterFactor*1/(d-20)**2
    F_x = F*(Center[0]-x)/d
    F_y = F*(Center[1]-y)/d
    return (F_x, F_y)


# Победи столько огров, сколько сможешь.
# Используй 'cast' и 'canCast' для заклинаний.
i = 0
while True:
    i += 1
    
    itIsSafeToHeal = True
    cannotFight = False
    
    enemy = hero.findNearestEnemy()
    if enemy:
        if enemy.type == "catapult":
            hero.moveXY(40, enemy.pos.y)
        if  hero.distanceTo(enemy) < 5:
            itIsSafeToHeal = False
            
        if hero.canCast("lightning-bolt", enemy):
            hero.cast("lightning-bolt", enemy)
            continue
        elif hero.canCast("chain-lightning", enemy):
            hero.cast("chain-lightning", enemy)
            continue
        elif hero.canCast("root", enemy):
            hero.cast("root", enemy)
            continue
        else:
            cannotFight = True
    
    if itIsSafeToHeal:
        if hero.canCast("regen", hero):
            hero.cast("regen", hero)
            continue
    
    deltaX, deltaY = 0, 0
    d = 1
    if enemy:
        deltaX = enemy.pos.x - hero.pos.x
        deltaY = enemy.pos.y - hero.pos.y
        d = norm(deltaX, deltaY)
    #F_x, F_y = 0, 0
    F_x, F_y = awayFromWalls(hero.pos.x, hero.pos.y)
    finalX = hero.pos.x-deltaX/d+F_x
    finalY = hero.pos.y-deltaY/d+F_y

    hero.moveXY(finalX, finalY)
    
    

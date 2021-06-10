def norm(x, y):
    return (x**2 + y**2)**0.5

def distance(x1, y1, x2, y2):
    deltaX = x2-x1
    deltaY = y2-y1
    return norm(deltaX, deltaY)

RepellingPoints = [
    (0, 48), # Upper Bound
    (5, 47),
    (10, 49),
    (13, 52),
    (19, 53),
    (24, 54),
    (24, 61),
    (29, 61),
    (34, 60),
    (39, 60),
    (0, 26), # Lower Bound
    (5, 28),
    (10, 27),
    (13, 21),
    (19, 16),
    (24, 15),
    (24, 9),
    (29, 7),
    (37, 7),
    (42, 9)
]
RepellingPoints += [(0, y) for y in range(27, 48, 5)] # Left Bound
RepellingPoints += [(43, y) for y in range(8, 62, 5)] # Right Bound
RepellingFactor = 5
def awayFromWalls(x, y):
    F_x, F_y = 0, 0
    for point in RepellingPoints:
        d = distance(x, y, point[0], point[1])
        F = RepellingFactor*1/d**2
        F_x = F*(point[0]-x)/d
        F_y = F*(point[1]-y)/d
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
    F_x, F_y = 0, 0
    #F_x, F_y = awayFromWalls(hero.pos.x, hero.pos.y)
    finalX = hero.pos.x-deltaX/d+F_x
    finalY = hero.pos.y-deltaY/d+F_y

    hero.moveXY(finalX, finalY)
    
    

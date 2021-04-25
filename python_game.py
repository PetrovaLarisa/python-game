import random

STEP = [1,2,3]   #список возможных шагов
STEPspec = [1,2,3,3]  #список возможных шагов с дополнительным шансом на излечение

class Gamer:

    def __init__(self,name,health=100):
        self.name = name
        self.health = health     
      
    def Move(self, currentMove):
        if currentMove == 1:
            delta=-random.randint(18, 25) #умеренный урон
        elif currentMove==2:
            delta=-random.randint(10, 35) #большой диапазон урона
        elif currentMove==3:
            delta=random.randint(18, 25)  #исцеление в небольшом диапазоне
        self.health=self.health+delta
        print ('Change in health of', self.name,'is',delta)
            
comp = Gamer('PC')
you = Gamer('Player')

while comp.health>0 and you.health>0:
    currentGamer=random.choice([comp, you])
    print (currentGamer.name,'makes a move. ', end='')
    if currentGamer==comp and currentGamer.health<=35:
        currentMove=random.choice(STEPspec)
    else:
        currentMove=random.choice(STEP)
    currentGamer.Move(currentMove)
    print ('PC has', comp.health,'health. Player has',you.health,'health.')
    
    

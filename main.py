import random

from evolved_creature import *

prey = EvolvedCreature(position=random.randint(1, 100), wings_quantity=random.randint(0, 2),
                       legs_quantity=random.randint(0, 2), teeth_sharpness_buff=random.choice(teeth_buffs),
                       claws_size_buff=random.choice(claws_buffs))
predator = EvolvedCreature(position=random.randint(0, prey.position - 1), wings_quantity=random.randint(0, 2),
                           legs_quantity=random.randint(0, 2), teeth_sharpness_buff=random.choice(teeth_buffs),
                           claws_size_buff=random.choice(claws_buffs))

print("")
while prey.do_move() or predator.do_move():
    print(f'Prey: {prey.position}\nPredator: {predator.position}\n')

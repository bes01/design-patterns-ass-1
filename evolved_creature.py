from body_parts import *
from creature import Creature


class EvolvedCreature(Creature):

    def __init__(self, position: int, wings_quantity, legs_quantity):
        self.position = position
        self.limbs = Wings(self, wings_quantity, Legs(self, legs_quantity, NoLimbs(self, 0)))

    def do_move(self) -> bool:
        return self.limbs.move()

    def do_damage(self):
        pass


thing = EvolvedCreature(0, 2, 2)

while thing.do_move():
    pass

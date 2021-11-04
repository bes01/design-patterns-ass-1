import random

from movement import *
from creature import Creature


class EvolvedCreature(Creature):

    def __init__(self, position: int, wings_quantity, legs_quantity):
        self.position = position

        # No Limbs: Crawling
        no_limbs = Limbs(self, 0)
        crawling = Movement(no_limbs, "Crawling", 0, 1, 1, 0)
        no_limbs.grant_movement_abilities(crawling)

        # Legs: Running, Walking and Hopping
        legs = Limbs(self, legs_quantity, no_limbs)
        legs_movement_chain = Movement(legs, "Running", 60, 4, 6, 2,
                                       Movement(legs, "Walking", 40, 2, 4, 2,
                                                Movement(legs, "Hopping", 20, 2, 3, 1)))
        legs.grant_movement_abilities(legs_movement_chain)

        # Wings: Flying
        wings = Limbs(self, wings_quantity, legs)
        flying = Movement(wings, "Flying", 80, 4, 8, 2)
        wings.grant_movement_abilities(flying)

        self.limbs_chain = wings

        print(f'The creature evolved {wings_quantity} wing(s) and {legs_quantity} leg(s) at position {self.position}')

    def do_move(self) -> bool:
        return self.limbs_chain.move()

    def do_damage(self):
        pass


prey = EvolvedCreature(position=random.randint(1, 100),
                       wings_quantity=random.randint(0, 2),
                       legs_quantity=random.randint(0, 2))
predator = EvolvedCreature(position=random.randint(0, prey.position - 1),
                           wings_quantity=random.randint(0, 2),
                           legs_quantity=random.randint(0, 2))

while prey.do_move() or predator.do_move():
    print(f'Prey: {prey.position}\nPredator: {predator.position}\n')

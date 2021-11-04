from creature import Creature
from movement import *

teeth_buffs = [3, 6, 9]
claws_buffs = [2, 3, 4]


class EvolvedCreature(Creature):

    def __init__(self, position: int, wings_quantity: int, legs_quantity: int,
                 teeth_sharpness_buff: int = 0, claws_size_buff: int = 1):
        self.position = position
        self.teeth_sharpness_buff = teeth_sharpness_buff
        self.claws_size_buff = claws_size_buff

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

        print(f'The creature evolved {wings_quantity} wing(s), {legs_quantity} leg(s), '
              f'+{self.teeth_sharpness_buff} teeth damage buff and *{self.claws_size_buff} claws'
              f' damage buff at position {self.position}')

    def do_move(self) -> bool:
        return self.limbs_chain.move()

    def do_damage(self) -> int:
        return self.claws_size_buff * (self.teeth_sharpness_buff + self.power)

    def receive_damage(self, damage: int) -> bool:
        self.health -= damage
        return self.health <= 0

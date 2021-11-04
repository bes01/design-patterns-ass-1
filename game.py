import random

from evolved_creature import *


# TODO: game simulation sketch
class Game:

    @staticmethod
    def hunt() -> None:
        Game.hunt(*Game.generate_creatures())

    @staticmethod
    def hunt(predator: Creature, prey: Creature) -> None:
        while prey.position > predator.position and predator.do_move():
            prey.do_move()

        if prey.position > predator.position:
            print('Pray ran into infinity')
        else:
            print('Fight for life')

    @staticmethod
    def generate_creatures() -> (Creature, Creature):
        prey = EvolvedCreature(position=random.randint(1, 100), wings_quantity=random.randint(0, 2),
                               legs_quantity=random.randint(0, 2), teeth_sharpness_buff=random.choice(teeth_buffs),
                               claws_size_buff=random.choice(claws_buffs))
        predator = EvolvedCreature(position=random.randint(0, prey.position - 1), wings_quantity=random.randint(0, 2),
                                   legs_quantity=random.randint(0, 2), teeth_sharpness_buff=random.choice(teeth_buffs),
                                   claws_size_buff=random.choice(claws_buffs))
        print("")

        return predator, prey

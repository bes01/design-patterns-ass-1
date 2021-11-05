import random

from evolved_creature import *


class Game:
    @staticmethod
    def hunt(prey: Creature, predator: Creature) -> None:
        while prey.position > predator.position and predator.do_move():
            prey.do_move()

        if prey.position > predator.position:
            print("Pray ran into infinity")
        else:
            print("Creatures started fighting")
            while not prey.receive_damage(predator.do_damage()) and not predator.receive_damage(prey.do_damage()):
                pass

            if predator.health > 0:
                print("Some R rated things have happened")
            else:
                print("Pray ran into infinity")

    @staticmethod
    def generate_creatures() -> (Creature, Creature):
        print("Generating prey...")
        prey = EvolvedCreature(
            position=random.randint(1, 100),
            wings_quantity=random.randint(0, 2),
            legs_quantity=random.randint(0, 2),
            teeth_sharpness_buff=random.choice(teeth_buffs),
            claws_size_buff=random.choice(claws_buffs),
        )
        print("Generating Predator...")
        predator = EvolvedCreature(
            position=random.randint(0, prey.position - 1),
            wings_quantity=random.randint(0, 2),
            legs_quantity=random.randint(0, 2),
            teeth_sharpness_buff=random.choice(teeth_buffs),
            claws_size_buff=random.choice(claws_buffs),
        )
        print("")

        return prey, predator

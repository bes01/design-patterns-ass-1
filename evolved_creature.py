from creature import Creature
from movement import Limbs, Movement, MovementType

teeth_buffs = [3, 6, 9]
claws_buffs = [2, 3, 4]


class EvolvedCreature(Creature):
    def __init__(
            self,
            position: int = 0,
            wings_quantity: int = 0,
            legs_quantity: int = 0,
            teeth_sharpness_buff: int = 0,
            claws_size_buff: int = 1,
            test_mode: bool = False
    ):
        self.position = position
        self.teeth_sharpness_buff = teeth_sharpness_buff
        self.claws_size_buff = claws_size_buff

        # No Limbs: Crawling
        no_limbs = Limbs(self, 0)
        crawling = Movement(no_limbs, *MovementType.CRAWLING.value)
        no_limbs.grant_movement_abilities(crawling)

        # Legs: Running, Walking and Hopping
        legs = Limbs(self, legs_quantity, no_limbs)
        legs_movement_chain = Movement(legs, *MovementType.RUNNING.value,
                                       Movement(legs, *MovementType.WALKING.value,
                                                Movement(legs, *MovementType.HOPPING.value)))
        legs.grant_movement_abilities(legs_movement_chain)

        # Wings: Flying
        wings = Limbs(self, wings_quantity, legs)
        flying = Movement(wings, *MovementType.FLYING.value)
        wings.grant_movement_abilities(flying)

        self.limbs_chain = wings

        if not test_mode:
            print(
                f"The creature evolved {wings_quantity} wing(s), {legs_quantity} "
                f"leg(s), +{self.teeth_sharpness_buff} teeth damage buff and "
                f"*{self.claws_size_buff} claws damage buff at position {self.position}\n"
            )

    def do_move(self) -> bool:
        return self.limbs_chain.move()

    def do_damage(self) -> int:
        return self.claws_size_buff * (self.teeth_sharpness_buff + self.power)

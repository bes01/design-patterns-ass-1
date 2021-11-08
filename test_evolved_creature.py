import random
from typing import List, Tuple, Any

from evolved_creature import EvolvedCreature
from movement import MovementType


def helper(evolved_creature: EvolvedCreature, movement_stats: List[Any]) -> Tuple[int, int]:
    position: int = evolved_creature.position
    stamina: int = evolved_creature.stamina

    while evolved_creature.stamina > movement_stats[1]:  # requires_stamina
        assert evolved_creature.do_move()
        position += movement_stats[3]  # speed
        stamina -= movement_stats[2]  # uses_stamina
        assert stamina == evolved_creature.stamina
        assert position == evolved_creature.position

    return stamina, position


# Movement Tests


def test_no_limb_evolved_creature() -> None:
    evolved_creature: EvolvedCreature = EvolvedCreature(test_mode=True)
    stamina, position = helper(evolved_creature, MovementType.CRAWLING.value)
    assert stamina == 0
    assert position == 100


def test_one_leg_evolved_creature() -> None:
    # Hop Until stamina = 20
    evolved_creature: EvolvedCreature = EvolvedCreature(legs_quantity=1, test_mode=True)
    stamina, position = helper(evolved_creature, MovementType.HOPPING.value)
    assert stamina == 20
    assert (
            position == 120
    )  # position = ((init_stamina - requires_stamina) / uses_stamina)) * speed

    # Crawl Until stamina = 0
    stamina, position = helper(evolved_creature, MovementType.CRAWLING.value)
    assert stamina == 0
    assert position == 140


def test_two_leg_evolved_creature() -> None:
    # Run Until stamina = 60
    evolved_creature: EvolvedCreature = EvolvedCreature(legs_quantity=2, test_mode=True)
    stamina, position = helper(evolved_creature, MovementType.RUNNING.value)
    assert stamina == 60
    assert position == 60

    # Continue By Walking Until stamina = 40
    stamina, position = helper(evolved_creature, MovementType.WALKING.value)
    assert stamina == 40
    assert position == 100


def test_two_wing_evolved_creature() -> None:
    # Run Until stamina = 60
    evolved_creature: EvolvedCreature = EvolvedCreature(wings_quantity=2, test_mode=True)
    stamina, position = helper(evolved_creature, MovementType.FLYING.value)
    assert stamina == 80
    assert position == 40


# Damage Tests


def test_receive_damage() -> None:
    evolved_creature = EvolvedCreature(test_mode=True)
    assert evolved_creature.health == 100

    assert not evolved_creature.receive_damage(50)  # Survived 50 damage
    assert evolved_creature.health == 50

    assert evolved_creature.receive_damage(51)  # More than enough to receive საბედისწერო damage


def test_do_damage_with_teeth_1() -> None:
    evolved_creature = EvolvedCreature(teeth_sharpness_buff=3, test_mode=True)
    assert evolved_creature.do_damage() == 4


def test_do_damage_with_teeth_2() -> None:
    evolved_creature = EvolvedCreature(teeth_sharpness_buff=4, test_mode=True)
    assert evolved_creature.do_damage() == 5


def test_do_damage_with_claws_1() -> None:
    evolved_creature = EvolvedCreature(claws_size_buff=3, test_mode=True)
    assert evolved_creature.do_damage() == 3


def test_do_damage_with_claws_2() -> None:
    evolved_creature = EvolvedCreature(claws_size_buff=6, test_mode=True)
    assert evolved_creature.do_damage() == 6


def test_do_damage_mixed_buffs() -> None:
    teeth_buff = random.randint(1, 10)
    claws_buff = random.randint(1, 10)
    evolved_creature = EvolvedCreature(
        teeth_sharpness_buff=teeth_buff, claws_size_buff=claws_buff, test_mode=True
    )
    assert evolved_creature.do_damage() == (1 + teeth_buff) * claws_buff

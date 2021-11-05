import pytest

from creature import Creature


@pytest.fixture()
def creature() -> Creature:
    return Creature(position=0)


def test_creature_init(creature: Creature) -> None:
    assert creature.position == 0
    assert creature.health == 100
    assert creature.power == 1
    assert creature.stamina == 100


def test_creature_movement(creature: Creature) -> None:
    assert not creature.do_move()  # Creature is not evolved, so it can't move


def test_creature_damage(creature: Creature) -> None:
    assert (
        creature.do_damage() == 1
    )  # Creature is not evolved, so it doesn't have any buffs


# Creature can survive 99 hits
def test_creature_receive_damage(creature: Creature) -> None:
    for i in range(99):
        assert creature.health > 0 and not creature.receive_damage(1)

    # 100th hit must be საბედისწერო
    assert creature.receive_damage(1)
    assert creature.health == 0

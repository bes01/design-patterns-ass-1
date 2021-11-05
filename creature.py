from dataclasses import dataclass


@dataclass
class Creature:
    position: int
    power: int = 1
    health: int = 100
    stamina: int = 100

    # Returns true if creature moved successfully otherwise false
    def do_move(self) -> bool:
        return False

    # Returns amount of dealt damage
    def do_damage(self) -> int:
        return 1

    # Returns true if received damage was საბედისწერო
    def receive_damage(self, damage: int) -> bool:
        self.health -= damage
        return self.health <= 0


@dataclass
class BodyPart:
    body: Creature

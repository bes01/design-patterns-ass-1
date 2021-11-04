from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol


@dataclass
class Creature(ABC):
    position: int
    power: int = 1
    health: int = 100
    stamina: int = 100

    # Returns true if creature moved successfully otherwise false
    @abstractmethod
    def do_move(self) -> bool:
        ...

    # Returns amount of dealt damage
    @abstractmethod
    def do_damage(self) -> int:
        ...

    # Returns true if received damage was საბედისწერო
    @abstractmethod
    def receive_damage(self, damage: int) -> bool:
        ...


@dataclass
class BodyPart(Protocol):
    body: Creature

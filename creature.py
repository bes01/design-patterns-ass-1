from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol


@dataclass
class Creature(ABC):
    position: int
    power: int = 1
    health: int = 100
    stamina: int = 100

    @abstractmethod
    def do_move(self):
        ...

    @abstractmethod
    def do_damage(self):
        ...


@dataclass
class BodyPart(Protocol):
    parentBody: Creature

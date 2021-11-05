from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Protocol, Optional

from creature import BodyPart


# [movement_type_str, requires_stamina, uses_stamina, speed, requires_limbs]
class MovementType(Enum):
    FLYING = ["Flying", 80, 4, 8, 2]
    RUNNING = ["Running", 60, 4, 6, 2]
    WALKING = ["Walking", 40, 2, 4, 2]
    HOPPING = ["Hopping", 20, 2, 3, 1]
    CRAWLING = ["Crawling", 0, 1, 1, 0]


class IMovement(ABC):
    @abstractmethod
    def move(self) -> bool:
        ...

    @abstractmethod
    def can_move(self) -> bool:
        ...


class ILimbs(Protocol):
    def move(self) -> bool:
        ...

    # Should be called once right after initialization
    def grant_movement_abilities(self, movement_chain: IMovement) -> None:
        ...


@dataclass
class Limbs(BodyPart):
    limbs_quantity: int
    limbs_chain: Optional[ILimbs] = None
    movement_chain: Optional[IMovement] = None

    def move(self) -> bool:
        if self.movement_chain is not None and self.movement_chain.can_move():
            return self.movement_chain.move()
        elif self.limbs_chain is not None:
            return self.limbs_chain.move()
        else:
            return False

    def grant_movement_abilities(self, movement_chain: IMovement) -> None:
        self.movement_chain = movement_chain


@dataclass
class Movement(IMovement):
    limb: Limbs
    type: str  # Just for printing
    requires_stamina: int
    uses_stamina: int
    speed: int
    requires_limbs: int
    movement_chain: Optional[IMovement] = None

    # Returns true if moved successfully and updates creature stats otherwise returns false
    def move(self) -> bool:
        if self.can_i_move():
            # print(self.type)
            self.limb.body.stamina -= self.uses_stamina
            self.limb.body.position += self.speed
            return True
        elif self.can_chain_move():
            return self.movement_chain.move()
        else:
            return False

    def can_move(self) -> bool:
        return self.can_i_move() or self.can_chain_move()

    def can_i_move(self):
        return (
            self.limb.limbs_quantity >= self.requires_limbs
            and self.limb.body.stamina > self.requires_stamina
            and self.limb.body.stamina - self.uses_stamina >= 0
        )

    def can_chain_move(self):
        return self.movement_chain is not None and self.movement_chain.can_move()

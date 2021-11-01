from abc import ABC, abstractmethod
from dataclasses import dataclass

from creature import BodyPart


@dataclass
class Limbs(BodyPart, ABC):
    limbs_quantity: int

    @abstractmethod
    def move(self) -> bool:
        ...


@dataclass
class Movement:
    limb: Limbs
    type: str
    requires_stamina: int
    uses_stamina: int
    speed: int

    # Returns true if moved successfully and updates creature stats otherwise returns false
    def move(self) -> bool:
        if self.can_move():
            print(self.type)
            self.limb.parentBody.stamina -= self.uses_stamina
            self.limb.parentBody.position += self.speed
            return True
        else:
            return False

    def can_move(self):
        return self.limb.parentBody.stamina > self.requires_stamina \
               and self.limb.parentBody.stamina - self.uses_stamina > 0


# Fly
@dataclass
class Wings(Limbs):
    other_type_of_limbs: Limbs

    def __post_init__(self):
        self.flying = Movement(self, "Flying", 80, 4, 8)

    def move(self) -> bool:
        if self.limbs_quantity == 2 and self.flying.can_move():
            return self.flying.move()
        else:
            return self.other_type_of_limbs.move()


# Run, Walk or Hop
@dataclass
class Legs(Limbs):
    other_type_of_limbs: Limbs

    def __post_init__(self):
        self.running = Movement(self, "Running", 60, 4, 6)
        self.walking = Movement(self, "Walking", 40, 2, 4)
        self.hopping = Movement(self, "Hopping", 20, 2, 3)

    def move(self) -> bool:
        if self.limbs_quantity == 2 and self.running.can_move():
            return self.running.move()
        elif self.limbs_quantity == 2 and self.walking.can_move():
            return self.walking.move()
        elif self.limbs_quantity == 1 and self.hopping.can_move():
            return self.hopping.move()
        else:
            return self.other_type_of_limbs.move()


# Crawl
@dataclass
class NoLimbs(Limbs):

    def __post_init__(self):
        self.crawling = Movement(self, "Crawling", 0, 1, 1)

    def move(self) -> int:
        if self.crawling.can_move():
            return self.crawling.move()
        else:
            return False

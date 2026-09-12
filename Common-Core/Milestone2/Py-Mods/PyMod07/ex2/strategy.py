from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capability import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    def __str__(self) -> str:
        return f"{self.args[0]}"


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            creature_msg = f"Invalid Creature '{creature.name}'"
            raise InvalidStrategyError(
                f"{creature_msg} for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            creature_msg = f"Invalid Creature '{creature.name}'"
            raise InvalidStrategyError(
                f"{creature_msg} for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

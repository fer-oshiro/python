from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self, *args: str, **kwargs: str) -> None:
        super().__init__(*args, **kwargs)
        self.is_transformed = False

    @abstractmethod
    def transform(self, target: str) -> str:
        pass

    @abstractmethod
    def revert(self, target: str) -> str:
        pass

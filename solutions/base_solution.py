from abc import ABC, abstractmethod


class BaseSolver(ABC):
    @classmethod
    @abstractmethod
    def solve(cls, s: str) -> int:
        pass

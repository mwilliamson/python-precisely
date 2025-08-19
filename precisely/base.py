from abc import ABC, abstractmethod
from .results import Result

class Matcher(ABC):
    @abstractmethod
    def match(self, actual) -> Result:
        pass

    @abstractmethod
    def describe(self) -> str:
        pass


def is_matcher(value):
    return isinstance(value, Matcher)

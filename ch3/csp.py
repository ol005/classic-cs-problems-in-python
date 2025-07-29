from typing import Generic, TypeVar
from abc import ABC, abstractmethod

V = TypeVar('V') # variable type
D = TypeVar('D') # domain type

class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: list[V]) -> None:
        self.variables = variables
    
    @abstractmethod
    def satisfied(self, assignment: dict[V, D]) -> bool:
        ...

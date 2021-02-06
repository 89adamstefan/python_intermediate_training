from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def drink(self):
        pass

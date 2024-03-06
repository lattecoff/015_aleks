from abc import ABC, abstractmethod


class Dishes(ABC):
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_cuisune(self):
        pass

""" End of file. """

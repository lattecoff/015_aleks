#import Dishes, MainCourses
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


class MainCourses(Dishes):
    def get_name(self):
        return self.name

    def get_cuisune(self):
        return self.cuisine


draniki = MainCourses('Dranki', 'Belorusian')
print(draniki.get_name())
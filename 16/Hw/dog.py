from animal_t_02 import Animal

class Dog(Animal):
    def voice(self):
        return 'Gau'

    def sleep(self):
        return 6

    def eat(self):
        return 1400


pongo = Dog('Pongo', 'Dalmatians', 'black-white')

print(pongo.name)
print(pongo.voice())
'''
Унаследуйте от класса Animal класс Cat, Dog, Hamster. Продумайте и реализуйте их логику.
'''

from animal import Animal

class Dog(Animal):
    def voice(self):
        return '\"gau\"'

    def sleep(self):
        return 6

    def eat(self):
        return 1400


pongo = Dog('Pongo', 'Dalmatians', 'black-white')

print(f'{pongo.name} say {pongo.voice()}.')

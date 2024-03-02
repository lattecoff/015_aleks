from animal import Animal

class Cat(Animal):
    def voice(self):
        return '\"myau\"'

    def sleep(self):
        return 8

    def eat(self):
        return 250


garfiled = Cat('Garfiled', 'British shorthair', 'red')

print(f'{garfiled.name} say {garfiled.voice()}.')

from animal_t_02 import Animal

class Cat(Animal):
    def voice(self):
        return 'Myau'

    def sleep(self):
        return 8

    def eat(self):
        return 250


garfiled = Cat('Garfiled', 'British shorthair', 'red')

print(garfiled.name)
print(garfiled.voice())
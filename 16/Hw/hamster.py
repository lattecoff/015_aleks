from animal_t_02 import Animal

class Hamster(Animal):
    def voice(self):
        return 'Ueee'

    def sleep(self):
        return 6

    def eat(self):
        return 1400


reeno = Hamster('Reeno', 'Syrian', 'red')

print(reeno.name)
print(reeno.voice())
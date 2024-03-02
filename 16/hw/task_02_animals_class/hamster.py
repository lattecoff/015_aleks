from animal import Animal

class Hamster(Animal):
    def voice(self):
        return '\"ueee\"'

    def sleep(self):
        return 6

    def eat(self):
        return 1400


reeno = Hamster('Reeno', 'Syrian', 'red')

print(f'{reeno.name} say {reeno.voice()}.')

'''
Задача
Спроектировать и реализовать класс:

🔹 минимум 4 метода;

🔹 минимум 2 статических свойства;

🔹 минимум 2 динамических свойства
'''
class Transformer:
    planet = 'Kybertron'
    isorganic = False

    def __init__(self, name, type, state, weapon,  health, x, y):
        self.name = name
        self.type = type
        self.state = state
        self.weapon = weapon
        self.health = health
        self.x = x
        self.y = y


    def transform_direct(self):
        """
        Меняет состояние трансформера из гуманоида в авто.
        :return:
        """
        if self.state == 'car':
            print('transform already finished.')
        else:
            self.state = 'car'

    def transform_reverse(self):
        """
        Меняет состояние трансформера из авто в гуманоида.
        :return:
        """
        if self.state == 'humanoid':
            print('transform already finished.')
        else:
            self.state = 'humanoid'

    def move(self, x, y):
        """
        Менят местоположение трансформера.
        :return:
        """
        self.x = x
        self.y = y

    def shoot(self, armor):
        """
        Атака.
        :return: возвращает процент урона.
        """
        if armor == 'basic':
            return 20
        elif armor == 'additional':
            return 35

    def about(self):
        """
        Возвращает параметры объекта.
        :return:.
        """
        print(self.name)
        print(self.type)
        print(self.state)
        print(self.health)
        print(self.x)
        print(self.y)


optimus = Transformer('Optimus', 'autobot', 'humanoid', 7, 100, 0, 0)

optimus.about()


class Animal:
    def __init__(self, name, breed, color):
        """
        :param name: Имя животного
        :param breed: Порода
        :param color: Цвет
        """
        self.name = name
        self.breed = breed
        self.color = color

    def voice(self):
        """
        Возпроизвести звук животного.
        :return:
        """
        pass

    def sleep(self):
        """
        Время которое необходимо животному
        :return:
        """
        pass

    def eat(self):
        """
        Порция еды в граммах, которое необходимо животному
        :return:
        """
        pass
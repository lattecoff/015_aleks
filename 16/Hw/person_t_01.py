class Person:
    def __init__(self, name):
        """
        :param name: Имя человека.
        """
        self.__name = name

    def get_name(self):
        """
        :return: Имя человека.
        """
        return self.__name


natalia = Person('Aleksandr')
print(natalia.get_name())

'''
Создайте класс Person с приватным атрибутом __name и публичным методом get_name(), который возвращает имя объекта. Затем создайте объект этого класса и вызовите метод get_name() для получения имени объекта.
'''
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


natasha = Person('Natasha')
print(natasha.get_name())
'''
Задача 2
Напишите функцию для проверки, совершенное ли число.
'''

from sympy import divisors


def is_perfect_number(num):
    '''
    Функция проверяет является число совершенным или нет.
    :param num - число.
    :return True - число соврешенное.
    :return False - число не совершенное.
    '''
    div_ls = divisors(num)

    if sum(div_ls[0:-1:]) == num:
        return True
    else:
        return False


number = input('Введите число: ')

if is_perfect_number(int(number)):
    print(f'Число {number} совершенное')
else:
    print(f'Число {number} не совершенное')
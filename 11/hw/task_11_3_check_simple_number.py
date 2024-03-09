'''
Задача 3
Напишите функцию для проверки, простое ли число.
'''

from sympy import primefactors


number = input('Введите число: ')

def is_prime_number(num):
    '''
    Функция проверяет является число простым или нет.
    :param num - число.
    :return True - число простое.
    :return False - число не простое.
    '''
    div_ls = primefactors(num)
    print(div_ls)

    if (div_ls[0]) == num:
        return True
    else:
        return False


if is_prime_number(int(number)):
    print(f'Число {number} простое')
else:
    print(f'Число {number} не простое')
import random
import secrets


print('1 - функция, которая принимает диапазон, генерирует и возвращает случайное целочисленное число.\n'
      '2 - функция, которая принимает диапазон, генерирует и возвращает случайное вещественное число.\n'
      '3 - функция, которая генерирует и возвращает случайное число.\n'
      '4 - функция, которая принимает список и возвращает перемешанный список.\n'
      '5 - функция, которая принимает список и возвращает случайный элемент из последовательности.'
      )

task = int(input('Введите номер функции которую хотите выполнить: '))


match task:
    case 1:
        def rand_number_from_range(range_str):
            """
            Функция, которая принимает диапазон, генерирует и возвращает случайное целочисленное число.
            :param range_str - диапазон в виде строки:
            :return случайное целочисленное число:
            """
            range_ls = range_str.split('-')

            bottom = int(range_ls[0])
            top = int(range_ls[1])

            return str(random.randint(bottom, top))


        range_str = input('Введите диапазон \'начало-конец\'')
        print(rand_number_from_range(range_str))

    case 2:
        def rand_number_from_range(range_str):
            """
            Функция, которая принимает диапазон, генерирует и возвращает случайное вещественное число.
            :param range_str - диапазон в виде строки:
            :return случайное вещественное число:
            """
            range_ls = range_str.split('-')

            bottom = float(range_ls[0])
            top = float(range_ls[1])

            return str((random.random()  *  top) + bottom)


        range_str = input('Введите диапазон \'начало-конец\'')
        print(rand_number_from_range(range_str))
    case 3:
        def get_random_number():
            """
            Функция, которая генерирует и возвращает случайное числ
            :return Возвращает число до 64 бит:
            """
            return secrets.randbelow(0xffffffffffffffff)

        print(get_random_number())

    case 4:
        def get_blend_list(ls_in):
            """
            Функция, которая принимает список и возвращает перемешанный список.
            :param ls - последовательность чисел:
            :return перемешанный список:
            """
            ls = ls_in.split()
            random.shuffle(ls)

            return ls

        series = input('Введите последовательность чисел, через пробел: ')
        print(get_blend_list(series))

    case 5:
        def get_rand_item(ls_in):
            """
            Функция, которая принимает список и возвращает случайный элемент из последовательности.
            :param ls - последовательность чисел:
            :return случайный элемент последовательности:
            """
            ls = ls_in.split()

            return secrets.choice(ls)

        series = input('Введите последовательность чисел, через пробел: ')
        print(get_rand_item(series))

    case _:
        print('такой задачи нет!')




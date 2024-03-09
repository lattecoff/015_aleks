'''
Задача 1
Напишите функцию, которая рекурсивно считает сумму чисел в списке.
'''

user_ls = [1,2,3,4,5,6,7,8,9] # 45.


def sum_numbers_in_list(ls):
    '''
    Вычисление суммы чисел в списке.
    :param ls - список чисел.
    По умолчанию равен нулю.
    :return сумма всех элементов списка.
    '''
    if ls == []:
        return 0
    else:
        return ls[-1] + sum_numbers_in_list(ls[:-1])


n = sum_numbers_in_list(user_ls)
print(n)
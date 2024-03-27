"""
Напишите функцию для вычисления факториала числа рекурсивно и итеративно. Факториал числа – это произведение от 1 до числа (10! = 1*2*3*4*5*6*7*8*9*10).
"""

numbers = int(input('Введите число для которого нужно вычислить факториал: '))

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1

    for i in range(2, n + 1):
        result *= i

    return result

print(factorial_recursive(numbers))
print(factorial_iterative(numbers))


"""
Используя синтаксический сахар, перепишите решение:
"""

a = input()
b = input()
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = []
for i in range(len(list1)):
    list2.append((list1[i], a, b))

print(list2)

list2 = [(item, a, b) for item in list1]
print('То же самое, с помощью синтаксического сахара.')
print(list2)
"""Для списка реализовать обмен значений соседних элементов, т.е.
значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

q = int(input("\n\t Введите количество элементов: "))
my_lst = []
for i in range(q):
    my_lst.append(input(f"Элемент # {i + 1} : "))
print(f"Список Ваших элементов:\n{my_lst}")
for x in range(0, (len(my_lst) - 1), 2):
    my_lst[x], my_lst[x+1] = my_lst[x+1], my_lst[x]
print(f"Изменёный список элементов:\n{my_lst}")

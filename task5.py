""" Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
    натуральных чисел. У пользователя необходимо запрашивать новый элемент
    рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
    то новый элемент с тем же значением должен разместиться после них.
    Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
    Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
    Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
    Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
    Набор натуральных чисел можно задать непосредственно в коде,
    например, my_list = [7, 5, 3, 3, 2]."""

rate_list = [7, 5, 3, 3, 2]
frq = int(input("Сколько чисел вы хотите добавить?\n\t ВВЕДИТЕ КОЛИЧЕСТВО: "))
for j in range(frq):
    add_new = int(input("Какое число Вы хотите добавить?\n\t ВВЕДИТЕ ЧИСЛО: "))
    if add_new in rate_list:
        i = rate_list.index(add_new)
        while (i + 1) <= (len(rate_list) - 1) \
                and (rate_list[i] == rate_list[i + 1]):
            i += 1
        rate_list.insert(i, add_new)
        print(f"Обновленный лист {rate_list}")
    else:
        if add_new <= rate_list[-1]:
            rate_list.append(add_new)
            print(f"Обновленный лист {rate_list}")
        else:
            rate_list.insert(0, add_new)
            print(f"Обновленный лист {rate_list}")

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
# одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка.
# Например, набор натуральных чисел:    7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]

a = False
while not a:
    try:
        new_score = int(input("Новый элемент рейтинга: "))
        if new_score < 0:
            print("Введите положительное число")
            continue
        if new_score > max(my_list):
            my_list.insert(0, new_score)
            break
        if new_score < min(my_list):
            my_list.append(new_score)
            break
        for i, el in enumerate(my_list):
            if my_list[-1] == new_score:
                my_list.append(new_score)
                a = True
                break
            if el == new_score and el != my_list[i + 1]:
                my_list.insert(i + 1, new_score)
                a = True
                break
    except ValueError:
        print("Ошибка. Вы ввели не натуральное число")

print(f"Измененный список {my_list}")
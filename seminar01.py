# Домашнее задание. Семинар №1
# 1. Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# print(a+b)

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
# seconds = int(input("Введите секунды: "))
# hour = seconds // 3600
# minutes = seconds // 60
# minutes2 = minutes % 10
# seconds_remains = seconds % 60
# print(hour, ":", minutes2, ":", seconds_remains)
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
# n = int(input("Введите число n: "))
# temp = str(n)
# n2 = temp + temp
# n3 = temp + temp + temp
# print(int(temp)+int(n2)+int(n3))


# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
#
# num = int(input("Введите число: "))
# max = num % 10
#
# max= num % 10
# num = num // 10
# while num > 0:
#     if num % 10 > max:
#         m = num % 10
#     num = num // 10
# print(max)


# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
#
# revenue = int(input("Введите сумму выручки: "))
# expenses = int(input("Введите сумму издержек: "))
#
# if revenue > expenses:
#     net_profit = revenue - expenses
#     print(f"Поздравляем, прибыль компании составила {net_profit}руб.")
# else:
#     net_loss = expenses - revenue


# # 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# # Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
#
# revenue = int(input("Введите сумму выручки: "))
# expenses = int(input("Введите сумму издержек: "))
#
# if revenue > expenses:
#     net_profit = revenue - expenses
#     print(f"Поздравляем, прибыль компании составила {net_profit}руб.")
#     print(f"Рентабильность компании составляем: {(net_profit/revenue) * 100}%")
# else:
#     net_loss = expenses - revenue
#
# people = int(input("Сколько человек работает в компании: "))
# rev_on_people = net_profit / people
# print(f"Получается, что на человека компания заработала: {rev_on_people}руб.")

# 7. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
#
# a = int(input("Введите результат первого дня: "))
# b = int(input("Введите искомое значение: "))
# day = 0
# while b - a > 0:
#     a = a + (a / 100 * 10)
#     day += 1
# print(day)

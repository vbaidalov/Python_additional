# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Введите число n: "))
temp = str(n)
n2 = temp + temp
n3 = temp + temp + temp
print(int(temp)+int(n2)+int(n3))
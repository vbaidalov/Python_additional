# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds = int(input("Введите секунды: "))
hour = seconds // 3600
minutes = seconds // 60
minutes2 = minutes % 10
seconds_remains = seconds % 60
print(hour, ":", minutes2, ":", seconds_remains)
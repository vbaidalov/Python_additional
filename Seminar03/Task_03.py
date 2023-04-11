# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.




# def my_func(a, b, c):
#     x = [a, b, c]
#     x.remove(min(a, b, c))
#     return sum(x)
#
# print(my_func(5, 80, 120))

def my_func(a, b, c):
    x = [a, b, c]
    x.remove(min(a, b, c))
    return sum(x)

print(my_func(int(input('Введите а: ')), int(input('Введите b: ')), int(input('Введите c: '))))

# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def user_data( *, name, lastname, birthday, city, email, phone):
    return print(f"имя: {name} фамилия: {lastname} "
                 f"год рождения: {birthday} "
                 f"город проживания: {city} "
                 f"email: {email} телефон: {phone}")

user_data(name=input('имя: '), lastname=input('фамилия: '),
              birthday=input('год рождения: '),
              city=input('город проживания: '),
              email=input('email: '),
              phone=input('phone: '),)
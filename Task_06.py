# 6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

revenue = int(input("Введите сумму выручки: "))
expenses = int(input("Введите сумму издержек: "))

if revenue > expenses:
    net_profit = revenue - expenses
    print(f"Поздравляем, прибыль компании составила: {net_profit}руб.")
    print(f"Рентабильность компании составляем: {(net_profit / revenue) * 100}%")
    people = int(input("Сколько человек работает в компании: "))
    rev_on_people = net_profit / people
    print(f"Прибыль компании в расчёте на одного сотрудника составила: {rev_on_people}руб.")

else:
    net_loss = expenses - revenue
    print(f"Компания отработала в минус {net_loss}руб.")
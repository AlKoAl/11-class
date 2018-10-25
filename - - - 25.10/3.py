# В комнату входят люди по очереди.
# Если у двух появившихся в комнате людей (один уже был, друго только что вошёл)
# одинаковые даты рождения (день и месяц), люди перестают входить в комнату.
# Найти мат.ожидание для количества вошедших людей.
import random
count = int(input("введите количество моделируемых ситуаций:"))
returns = [0 for i in range(366)]
for i in range(count):
    birthdays = []
    while len(birthdays) < 365:
        month = random.randint(1, 12)  # выбираем месяц рождения
        if month in [1, 3, 5, 7, 8, 10, 12]:  # выборы даты
            day = random.randint(1, 31)
        elif month == 2:
            day = random.randint(1, 28)
        else:
            day = random.randint(1, 30)
        print("{day}/{month}".format(day=day, month=month))
        if "{day}/{month}".format(day=day, month=month) in birthdays:  # если такая дата уже есть в списке дней рожд.
            break
        else:
            birthdays.append("{day}/{month}".format(day=day, month=month))
    returns[len(birthdays) + 1] = returns[len(birthdays) + 1] + 1  # len(birthdays) + 1 т.к.
    #  надо посчитать последнего пришедшего (из-за break он не записывается)
    print("ok")
print(returns)
answer = 0
for i in range(366):
    answer += i * returns[i]/count
    print(answer)
print(answer)

"""
Задача по поиску численноисти популяции кроликов со следующими условиями:
Мы считаем, что кролики сначала подвергаются выеданию, потом начинают размножаться. То есть, если
к началу сезона у нас было K кроликов, то каждый из них будет съеден с заданной вероятностью
Новопоявившийся кролик начинает существовать только со следующего месяца
То есть, изначальный кролик даст потомство только на четвёртый сезон, при условии, что А = 3
Кролики вначале дают потомство, затем умирают в последний сезон.
"""
import random


def population(n, a, baby, c, p, lst, i):
    global Count
    if a >= c:
        return "Кролики не размножаются"
    if n >= 10**11:
        return "Кролики съели всё живое"
    elif i == Count:
        return "количество кроликов на {} сезоне: {}".format(Count, n)
    else:
        for j in range(len(lst)):
            count = 0
            for mbeaten in range(lst[j]):
                try:  # работает даже если кроликов не едят p == 0
                    if random.randint(0, int(1/p)) == 0:
                        count += 1
                        n -= 1
                except:
                    pass
            lst[j] = lst[j] - count   # съели кроликов
        if len(lst) <= a:
            lst.append(0)
        elif c > len(lst) > a:
            n += sum([k * baby for k in lst[0:len(lst) - a]])
            lst = lst + [sum([k * baby for k in lst[0:len(lst) - a]])]
        else:
            n += sum([k * baby for k in lst[0:len(lst) - a]]) - lst[0]
            lst = lst[1:] + [sum([k * baby for k in lst[0:len(lst) - a]])]
        return population(n, a, baby, c, p, lst, i=i + 1)


A = int(input("Введите количество сезонов до взрослого состояния: "))
B = int(input("Введите количество пар особей воспроизводимых одной парой: "))
C = int(input("Введите длительность жизни кроликов в сезонах: "))
P = float(input("Введите вероятность быть съеденными хищниками(в виде десятичной дроби): "))
Count = int(input("Введите количество интересующих вас сезонов: "))
print(population(1, A, B, C, P, [1], 1))

def body():
    points = []  # список, в который мы будем сохранять, вводимые точки
    for i in range(int(input("Введите количество координат"))):
        points.append(list(map(float, input().split())))
    points.sort(key=lambda x: x[0])  # отсортировали точки по возрастанию координаты по оси Ox

    for i in range(len(points[:-1])):
        points[i] += approximate(points[i], points[i + 1])
    # Создали список, в котором лежат последовательные по x координаты, в первой из каждых двух координат
    # находятся коэффициенты A, B, C для уравнения прямой Ax+By+C = 0

    # На позицию 0 поставить вероятность для данного случайного события x
    for i in range(1, len(points)):
        points[-i].insert(0, points[-i][1] - points[-i - 1][1])
    points[0].insert(0, points[0][1])
    while int(input("Если вы хотите узнать значение функции вероятности в точке, введите 1, иначе 0:")):
        print(return_y(float(input("Введите координату по оси Ox")), points))
    return expect_val_discrete(points), dispersion_discrete(points)


def approximate(x, y):
    # Приписывает после координат точек (всех, кроме последней по оси Ox) значения
    # линейных функций (A, B, C: Ax+By+C = 0) между ней и первой точкой (по Ox), встерчающейся справа
    x1, y1 = x
    x2, y2 = y
    return [y1 - y2, x2 - x1, x1 * y2 - x2 * y1]


def return_y(x, points):  # x - координата по х
    # Возвращение f(x)
    if x >= points[0][1]:
        for i in range(len(points[:-1])):
            try:
                if x > points[i][1]:
                    return (points[i][3]*x + points[i][5]) / (-points[i][4])
            except:
                return "За пределами распределения"
    else:
        return "За пределами распределения"


def expect_val_discrete(massive):
    # считает математическое ожидание
    E = 0
    for i in massive:
        E += i[0]*i[1]
    return E


def dispersion_discrete(massive):
    # считает дисперсию
    D = 0
    E = expect_val_discrete(massive)
    for i in massive:
        D += (i[1]-E)**2*i[0]
    return D


""" Так как я так и не понял, что от нас требовалось, я сделал задачу со следующим условием:
Программа спрашивет количество вводимых точек (как сделать так, чтобы их было произвольное количество я не помню)
После этого на вход подаются точки, обладающие следующими свойствами:
1) координата по Oy лежит на отрезке [0 , 1]
2) F(x) не убывает, т.е. если x1 < x2, то F(x1) < F(x2)
и т.д. (свойства функции распределения) дальнейшие пояснения в комментариях при функциях
"""
print(body()) # Всегда возвращает кортеж из значений матожидания и дисперсии

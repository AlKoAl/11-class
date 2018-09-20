"""
Программа считает биномиальный коэффицент, получая на вход n и k соответственно.
При рекурсивном обрацении к (n-1, k-1) и (n-1, k) первое найденное значение
запоминается в локальной матрице объемлющей функции
матрица при созлании содержит 1, как первый символ каждой строки, за которым следует
некоторое количество -1
"""
n, k = map(int, input().split())  # считали n и k


def encompassing(n, k):  # Объемлющая функция
    matrix = []  # Локальная матрица
    border = 1  # Счётчик количества столбцов
    for i in range(n + 1):  # задание строк матрицы
        matrix.append([])  # добавление новой строки
        if border == k + 2:  # если количество столбцов равно кол-ву столбцов до нужного k
            matrix[i].append(1)  # Первый элемент всегда 1
            for j in range(1, k+2):  # заполнить оставшиеся -1
                matrix[i].append(-1)
        else:
            matrix[i].append(1)
            for g in range(1, border):
                matrix[i].append(-1)
            border += 1

    def internal(n, k):
        nonlocal matrix  # ссылка на объект объемлющей функции
        if n == k-1:
            return 0
        if matrix[n][k] == -1:
            matrix[n][k] = internal(n - 1, k - 1) + internal(n - 1, k)
        return matrix[n][k]
    internal(n, k)
    return matrix[n][k]


try:
    print(encompassing(n, k))
except:
    print("Ошибка")

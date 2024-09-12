# Функция поиска вариантов для условия, что i = 3**K * 5**L * 7**M
import math


def find_variants(x):
    variants = []
    for K in range(int(math.log(x, 3)) + 1):
        for L in range(int(math.log(x, 5))+1):
            for M in range(int(math.log(x, 7))+1):
                if 3**K*5**L*7**M <= x:
                    variants.append(3**K*5**L*7**M)
    variants.sort()
    return variants


x = int(input("Введите x, он должен быть натуральным числом: "))
if x <= 0:
    print("x должен быть натуральным числом!")
else:
    result = []
    result = find_variants(x)

    print(result)
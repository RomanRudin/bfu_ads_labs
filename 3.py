# Функция поиска вариантов для условия, что i = 3**K * 5**L * 7**M
def find_variants(i):
    variants = []
    for K in range(int(i/3)+1):
        for L in range(int(i/5)+1):
            for M in range(int(i/7)+1):
                if 3**K * 5**L * 7**M == i:
                    variants.append((K, L, M))
    return variants


x = int(input("Введите x, он должен быть натуральным числом!: "))
if x <= 0:
    print("x должен быть натуральным числом!")
else:
    for i in range(1, x + 1):
        variants = find_variants(i)
        print(f"Число {i}:")
        if variants:
            for K, L, M in variants:
                print("K:", K, "L:", L, "M:", M, "i:", i)
        else:
            print(f"Число {i} не подходит :(")

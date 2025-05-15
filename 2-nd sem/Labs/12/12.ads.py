# Решить дискретную задачу о рюкзаке, использовать перебор

def knapsack_bruteforce(values, weights, capacity):
    n = len(values)
    max_value = 0
    best_subset = []
    for i in range(1, 2 ** n):
        subset = []
        total_weight = 0
        total_value = 0
        for j in range(n):
            if (i >> j) & 1:
                subset.append(j)
                total_weight += weights[j]
                total_value += values[j]
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            best_subset = subset.copy()

    return max_value, best_subset


if __name__ == "__main__":
    values = [60, 100, 120]  # Стоимости предметов
    weights = [10, 20, 30]  # Веса предметов
    capacity = 50  # Вместимость рюкзака

    max_value, best_subset = knapsack_bruteforce(values, weights, capacity)

    print("Максимальная стоимость:", max_value)
    print("Выбранные предметы (индексы):", best_subset)
    print("Выбранные предметы (веса):", [weights[i] for i in best_subset])
    print("Выбранные предметы (стоимости):", [values[i] for i in best_subset])

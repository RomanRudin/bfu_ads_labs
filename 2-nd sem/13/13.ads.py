# Решить задачу о раскладке по ящикам. Необходимо использовать динамическое программирование по подмножествам.

def bin_packing(items, bin_capacity):
    n = len(items)
    subset_info = []
    for mask in range(1, 1 << n):
        total_weight = 0
        elements = []
        for i in range(n):
            if mask & (1 << i):
                total_weight += items[i]
                elements.append(items[i])
        if total_weight <= bin_capacity:
            subset_info.append((mask, total_weight))

    dp = [float('inf')] * (1 << n)
    dp[0] = 0

    for mask in range(1 << n):
        if dp[mask] == float('inf'):
            continue
        for subset, weight in subset_info:
            if (mask & subset) == 0:
                new_mask = mask | subset
                if dp[new_mask] > dp[mask] + 1:
                    dp[new_mask] = dp[mask] + 1

    return dp[(1 << n) - 1]


if __name__ == "__main__":
    items = [2, 5, 4, 7, 1, 3, 8]
    bin_capacity = 10

    min_bins = bin_packing(items, bin_capacity)
    print(f"Минимальное количество ящиков: {min_bins}")

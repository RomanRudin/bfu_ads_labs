"""
Задача коммивояжёра - поиск кратчайшего возможного маршрута,
который проходит через заданный набор городов и возвращается в начальный город.
Маршруты заданы матрицей связности.
Необходимо использовать динамическое программирование по подмножествам.
"""

import sys


def tsp_dp(dist):
    n = len(dist)
    subset_size = 1 << n
    dp = [[float('inf')] * n for _ in range(subset_size)]
    dp[1][0] = 0

    for mask in range(subset_size):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if u == v:
                    continue
                if mask & (1 << v):
                    new_cost = dp[mask ^ (1 << u)][v] + dist[v][u]
                    if new_cost < dp[mask][u]:
                        dp[mask][u] = new_cost

    full_mask = (1 << n) - 1
    min_cost = float('inf')
    for u in range(1, n):
        candidate_cost = dp[full_mask][u] + dist[u][0]
        if candidate_cost < min_cost:
            min_cost = candidate_cost

    return min_cost


if __name__ == "__main__":
    dist = [
        [0, 10, 15, 20],  # Расстояния из города 0
        [10, 0, 35, 25],   # Расстояния из города 1
        [15, 35, 0, 30],   # Расстояния из города 2
        [20, 25, 30, 0]    # Расстояния из города 3
    ]

    min_path_cost = tsp_dp(dist)
    print("Минимальная стоимость маршрута коммивояжёра:", min_path_cost)

import sys
from typing import List, Tuple

def tsp_with_path(dist: List[List[int]], start: int) -> Tuple[int, List[int]]:
    n = len(dist)
    total_mask = (1 << n) - 1

    dp = [[sys.maxsize] * n for _ in range(total_mask + 1)]
    parent = [[-1] * n for _ in range(total_mask + 1)]
    dp[1 << start][start] = 0

    for mask in range(total_mask + 1):
        for i in range(n):
            if not (mask & (1 << i)):
                continue

            for j in range(n):
                if mask & (1 << j):
                    continue

                if dp[mask][i] != sys.maxsize and dp[mask][i] + dist[i][j] < dp[mask | (1 << j)][j]:
                    dp[mask | (1 << j)][j] = dp[mask][i] + dist[i][j]
                    parent[mask | (1 << j)][j] = i

    min_cost = sys.maxsize
    last_city = -1
    for i in range(n):
        if i == start:
            continue
        if dp[total_mask][i] != sys.maxsize and dp[total_mask][i] + dist[i][start] < min_cost:
            min_cost = dp[total_mask][i] + dist[i][start]
            last_city = i

    path = []
    mask = total_mask
    current = last_city
    while current != -1:
        path.append(current)
        prev = parent[mask][current]
        mask ^= (1 << current)
        current = prev
    path.reverse()
    path.append(start)

    return min_cost, path



if __name__ == "__main__":
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    min_cost, path = tsp_with_path(dist, 0)

    print("The optimal route:", " -> ".join(map(str, path)))
    print(min_cost)
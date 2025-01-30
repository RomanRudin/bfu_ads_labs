def backpack(W, wt, val, n) -> int:
    data = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                data[i][w] = max(val[i - 1] + data[i - 1][w - wt[i - 1]], data[i - 1][w])
            else:
                data[i][w] = data[i - 1][w]

    return data[n][W]
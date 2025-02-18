def backpack(max_weight: int, n: int, weights_list: list[int], value: list[int]) -> int:
    data = [[0] * (max_weight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for weight in range(1, max_weight + 1):
            if weights_list[i - 1] <= weight:
                data[i][weight] = max(value[i - 1] + data[i - 1][weight - weights_list[i - 1]], data[i - 1][weight])
            else:
                data[i][weight] = data[i - 1][weight]

    return data[n][max_weight]


if __name__ == "__main__":
    print(backpack(10, 5, [1, 2, 3, 4, 10], [2, 3, 7, 9, 20])) #? Expected 21
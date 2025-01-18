def coin_change(coins: list, amount):
    data = [float('inf')] * (amount+1)
    data[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if coin <= i:
                data[i] = min(data[i], data[i-coin] + 1)

    return data[amount] if data[amount] != float('inf') else -1
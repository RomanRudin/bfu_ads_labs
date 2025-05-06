from typing import Literal


def coin_exchange(coins: list, amount: int) -> float | Literal[-1]:
    data = [float('inf')] * (amount + 1)
    data[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                data[i] = min(data[i], data[i - coin] + 1)

    return data[amount] if data[amount] != float('inf') else -1


if __name__ == "__main__":
    print(coin_exchange([1, 3, 4], 6))         #? Expected 2
    print(coin_exchange([1], 10))              #? Expected 10
    print(coin_exchange([1, 2, 5], 100))       #? Expected 20
    print(coin_exchange([3, 5], 7))            #? Expected -1
    print(coin_exchange([1, 5, 10, 25], 30))   #? Expected 2
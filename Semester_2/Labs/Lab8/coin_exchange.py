from typing import List, Union, Literal

def coin_exchange(coins: List[int], amount: int) -> Union[int, Literal[-1]]:
    if amount < 0:
        return -1
    if amount == 0:
        return (0, [])

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[amount] == float('inf'):
        return -1

    coins_used = []
    remaining = amount
    while remaining > 0:
        coin = coin_used[remaining]
        coins_used.append(coin)
        remaining -= coin

    return (dp[amount], coins_used)


if __name__ == "__main__":
    print(coin_exchange([1, 3, 4], 6))         #? Expected 2
    print(coin_exchange([1], 10))              #? Expected 10
    print(coin_exchange([1, 2, 5], 100))       #? Expected 20
    print(coin_exchange([3, 5], 7))            #? Expected -1
    print(coin_exchange([1, 5, 10, 25], 30))   #? Expected 2

# Проблема размена монет: поиск количества способов внести сдачу на заданную сумму денег,
# используя заданный набор номиналов монет.

def count_ways_to_make_change(S, coins):
    dp = [0] * (S + 1)
    dp[0] = 1

    for coin in coins:
        for amount in range(coin, S + 1):
            dp[amount] += dp[amount - coin]

    return dp[S]


if __name__ == "__main__":
    coins = [1, 2, 5]  # Номиналы монет
    S = 5  # Сумма для размена
    print("Количество способов размена:", count_ways_to_make_change(S, coins))

def backpack(W: int, weights: list[int], values: list[int], n: int) -> int:
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], 
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][W]
    
    

if __name__ == "__main__":
    print(backpack(10, [2, 3, 5, 7], [10, 15, 20, 25], 4)) #? Expected 45
    print(backpack(10, [1, 2, 3, 4, 10], [2, 3, 7, 9, 20], 5)) #? Expected 21
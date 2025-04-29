def egg_drop(eggs, floors) -> int:
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]
    
    for m in range(1, floors + 1):
        dp[1][m] = m
    
    for k in range(2, eggs + 1):
        for m in range(1, floors + 1):
            dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1
    
    min_throws = -1
    for m in range(1, floors + 1):
        if dp[eggs][m] >= floors:
            min_throws = m
            break
    
    if min_throws != -1:
        print("Strategy of throws:")
        remaining_throws = min_throws
        current_floor = 0
        step = dp[eggs - 1][remaining_throws - 1] + 1
        
        while remaining_throws > 0:
            current_floor += step
            print(f"Throw from floor: {current_floor}")
            remaining_throws -= 1
            if current_floor >= floors:
                break
            step = dp[eggs - 1][remaining_throws - 1] + 1
    
    return min_throws



if __name__ == "__main__":
    print(egg_drop(2, 100)) #? Expected 14
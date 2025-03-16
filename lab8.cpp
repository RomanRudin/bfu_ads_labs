#include "lab8.h" 
#include <iostream>
#include <vector>

int coin_change_ways(const std::vector<int>& coins, int amount) {
    std::vector<int> dp(amount + 1, 0);  
    dp[0] = 1;  

    for (int coin : coins) {
        for (int i = coin; i <= amount; ++i) {
            dp[i] += dp[i - coin];
        }
    }

    return dp[amount];
}

int main() {
    std::vector<int> coins = { 1, 2, 5 };  
    int amount = 5; 
    int ways = coin_change_ways(coins, amount);

    std::cout << "coin_change_ways: " << ways << std::endl;

    return 0;
}
// #include "lab12.h"
#include <iostream>
#include <vector>
#include <algorithm>

int knapsack(int W, const std::vector<int>& weights, const std::vector<int>& values, int n) {
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(W + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (weights[i - 1] <= w) {
                dp[i][w] = std::max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]);
            }
            else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[n][W];
}

int main() {
    int W = 10; 
    std::vector<int> weights = { 2, 3, 5, 7 }; 
    std::vector<int> values = { 10, 15, 20, 25 }; 
    int n = weights.size(); 

    int maxValue = knapsack(W, weights, values, n);

    std::cout << "Максимальная стоимость: " << maxValue << std::endl;

    return 0;
}
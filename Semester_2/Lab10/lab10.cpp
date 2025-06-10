// #include "lab10.h"
#include <iostream>
#include <vector>

int egg_drop_with_strategy(int eggs, int floors) {
    std::vector<std::vector<int>> dp(eggs + 1, std::vector<int>(floors + 1, 0));

    for (int m = 1; m <= floors; ++m) {
        dp[1][m] = m;
    }
    for (int k = 2; k <= eggs; ++k) {
        for (int m = 1; m <= floors; ++m) {
            dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1;
        }
    }
    int min_throws = -1;
    for (int m = 1; m <= floors; ++m) {
        if (dp[eggs][m] >= floors) {
            min_throws = m;
            break;
        }
    }
    if (min_throws != -1) {
        std::cout << "Strategic of throw:" << std::endl;
        int remaining_throws = min_throws;
        int current_floor = 0;
        int step = dp[eggs - 1][remaining_throws - 1] + 1;

        while (remaining_throws > 0) {
            current_floor += step;
            std::cout << "Throw from the floor: " << current_floor << std::endl;
            remaining_throws--;
            if (current_floor >= floors) {
                break;
            }
            step = dp[eggs - 1][remaining_throws - 1] + 1;
        }
    }
    return min_throws;
}

int main() {
    int eggs = 2;
    int floors = 100;

    int min_throws = egg_drop_with_strategy(eggs, floors);
    std::cout << "min n: " << min_throws << std::endl;

    return 0;
}

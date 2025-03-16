#include "lab9.h"
#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
int tsp_with_path(const std::vector<std::vector<int>>& dist, int start) {
    int n = dist.size();
    int totalMask = (1 << n) - 1;

    std::vector<std::vector<int>> dp(totalMask + 1, std::vector<int>(n, INT_MAX));
    std::vector<std::vector<int>> parent(totalMask + 1, std::vector<int>(n, -1));
    dp[1 << start][start] = 0;

    for (int mask = 1; mask <= totalMask; ++mask) {
        for (int i = 0; i < n; ++i) {
            if (!(mask & (1 << i))) continue;

            for (int j = 0; j < n; ++j) {
                if (mask & (1 << j)) continue;

                if (dp[mask][i] != INT_MAX && dp[mask][i] + dist[i][j] < dp[mask | (1 << j)][j]) {
                    dp[mask | (1 << j)][j] = dp[mask][i] + dist[i][j];
                    parent[mask | (1 << j)][j] = i;
                }
            }
        }
    }

    int min_сost = INT_MAX;
    int last_сity = -1;
    for (int i = 0; i < n; ++i) {
        if (i == start) continue;
        if (dp[totalMask][i] != INT_MAX && dp[totalMask][i] + dist[i][start] < min_сost) {
            min_сost = dp[totalMask][i] + dist[i][start];
            last_сity = i;
        }
    }

    std::vector<int> path;
    int mask = totalMask;
    int current = last_сity;
    while (current != -1) {
        path.push_back(current);
        int prev = parent[mask][current];
        mask ^= (1 << current);
        current = prev;
    }
    std::reverse(path.begin(), path.end());
    path.push_back(start);

    std::cout << "The optimal route: ";
    for (size_t i = 0; i < path.size(); ++i) {
        std::cout << path[i];
        if (i < path.size() - 1) std::cout << " -> ";
    }
    std::cout << std::endl;

    return min_сost;
}

int main() {
    std::vector<std::vector<int>> dist = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };

    int start = 0;
    int min_сost = tsp_with_path(dist, start);

    std::cout << "min cost of a route : " << min_сost << std::endl;

    return 0;
}

// #include "lab13.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

void backtrack(const std::vector<int>& weights, int capacity, int start, std::vector<int>& bins, int& min_bins) {
    if (start == weights.size()) {
        min_bins = std::min(min_bins, static_cast<int>(bins.size()));
        return;
    }
    for (size_t i = 0; i < bins.size(); ++i) {

        if (bins[i] + weights[start] <= capacity) {
            bins[i] += weights[start];
            backtrack(weights, capacity, start + 1, bins, min_bins);
            bins[i] -= weights[start]; // Откат (backtracking)
        }
    }
    bins.push_back(weights[start]);
    backtrack(weights, capacity, start + 1, bins, min_bins);
    bins.pop_back(); // Откат (backtracking)
}


int bin_packing_subset(const std::vector<int>& weights, int capacity) {
    int min_bins = INT_MAX; 
    std::vector<int> bins; 
    backtrack(weights, capacity, 0, bins, min_bins);
    return min_bins;
}

int main() {
    std::vector<int> weights = { 4, 5, 2, 1, 3 };
    int capacity = 6;

    int result = bin_packing_subset(weights, capacity);
    std::cout << "min num bins: " << result << std::endl;

    return 0;
}

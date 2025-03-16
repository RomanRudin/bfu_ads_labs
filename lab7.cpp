#include "lab7.h" 
#include <iostream>
#include <vector>
#include <climits>  
int kadane_algorithm(const std::vector<int>& nums, std::vector<int>& subarray) {
    int max_sum = INT_MIN;  
    int current_sum = 0;
    int start = 0;          
    int end = 0;           
    int temp_start = 0;

    for (int i = 0; i < nums.size(); ++i) {
        current_sum += nums[i];

        if (current_sum > max_sum) {
            max_sum = current_sum;
            start = temp_start;
            end = i;
        }
        if (current_sum < 0) {
            current_sum = 0;
            temp_start = i + 1;
        }
    }
    for (int i = start; i <= end; ++i) {
        subarray.push_back(nums[i]);
    }

    return max_sum;
}

int main() {
    std::vector<int> nums = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
    std::vector<int> subarray;
    int max_sum = kadane_algorithm(nums, subarray);
    std::cout << "Maximum amount of a subarray: " << max_sum << std::endl;

    std::cout << "subarray with max amount: ";
    for (int num : subarray) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    return 0;
}


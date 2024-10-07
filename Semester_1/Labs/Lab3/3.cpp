#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> answer;
    int x;
    std::cout << "Please, enter x: " << std::endl;
    std::cin >> x;
    int maxPow = (int)(log(x) / log(3)) + 1;
    for (int k; k < maxPow; k++) {
        for (int l = 0; l < maxPow - k; l++) {
            for (int m = 0; m < maxPow - k - l; m++) {
                int number = pow(3, k) * pow(5, l) * pow(7, m);
                if ((number <= x) && (std::find(answer.begin(), answer.end(), number) == answer.end())) 
                    answer.push_back(number);
            }
        }
    }
    std::sort(answer.begin(), answer.end());
    std::cout << "The answer:" << std::endl;
    for (int i = 0; i < answer.size(); i++) {
        std::cout << answer[i] << std::endl;
    }
    return 0;
}
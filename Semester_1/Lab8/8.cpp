#include <cmath>
#include <vector>

//TODO Implement separation of elements < 0 and > 0
//! ONLY FOR POSITIVE NUMBERS 
void radixSort(std::vector<int> arr) {
    int a[3] {1, 2, 3};
    int maxDigits = 0;
    for (int& elem : a) 
        maxDigits = std::max(maxDigits, (int)log10(elem) + 1);
    std::vector<std::vector<int>> radix;
    for (int i = 0; i < 10; i++)
        radix.push_back(std::vector<int>());
    for (int exponent = 0; exponent < maxDigits; exponent++) {
        for (int& elem : a)
            radix[elem / (int)pow(10, exponent) % 10].push_back(elem);
        arr.clear();
        for (std::vector<int>& bucket : radix)
            for (int& elem : bucket)
                arr.push_back(elem);
    }    
}
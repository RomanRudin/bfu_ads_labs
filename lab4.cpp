#include "lab4.h"
#include <iostream>
#include <vector>
#include <string>

std::vector<int> compute_prefix_function(const std::string& pattern) {
    int m = pattern.length();
    std::vector<int> prefix(m, 0);
    int k = 0;  

    for (int i = 1; i < m; ++i) {
        while (k > 0 && pattern[k] != pattern[i]) {
            k = prefix[k - 1];
        }
        if (pattern[k] == pattern[i]) {
            k++;
        }
        prefix[i] = k; 
    }
    return prefix;
}


void kmp_search(const std::string& text, const std::string& pattern) {
    int n = text.length();
    int m = pattern.length();
    std::vector<int> prefix = compute_prefix_function(pattern);  
    int q = 0;  

    for (int i = 0; i < n; ++i) {
        while (q > 0 && pattern[q] != text[i]) {
            q = prefix[q - 1];
        }
        if (pattern[q] == text[i]) {
            q++;
        }
        if (q == m) {
            std::cout << "The sample was found at the position:" << i - m + 1 << std::endl;
            q = prefix[q - 1];  
        }
    }
}

int main() {
    std::string text = "ababcababacababcababacababcababacababcababacababcababacababcababacababcababac";
    std::string pattern = "ababac";

    kmp_search(text, pattern);

    return 0;
}
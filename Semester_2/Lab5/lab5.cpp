#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

std::unordered_map<char, int> build_bad_char_table(const std::string& pattern) {
    std::unordered_map<char, int> badCharTable;
    int m = pattern.length();

    for (int i = 0; i < m - 1; ++i) {
        badCharTable[pattern[i]] = m - 1 - i;
    }
    return badCharTable;
}
std::vector<int> build_good_suffix_table(const std::string& pattern) {
    int m = pattern.length();
    std::vector<int> goodSuffixTable(m, m);
    std::vector<int> suffix(m, 0);

    for (int i = m - 2; i >= 0; --i) {
        int j = i;
        while (j >= 0 && pattern[j] == pattern[m - 1 - i + j]) {
            --j;
        }
        suffix[i] = i - j;
    }

    for (int i = 0; i < m; ++i) {
        goodSuffixTable[i] = m;
    }

    for (int i = m - 1; i >= 0; --i) {
        if (suffix[i] == i + 1) {
            for (int j = 0; j < m - 1 - i; ++j) {
                if (goodSuffixTable[j] == m) {
                    goodSuffixTable[j] = m - 1 - i;
                }
            }
        }
    }

    for (int i = 0; i < m - 1; ++i) {
        goodSuffixTable[m - 1 - suffix[i]] = m - 1 - i;
    }
    return goodSuffixTable;
}
void boyer_moore_search(const std::string& text, const std::string& pattern) {
    int n = text.length();
    int m = pattern.length();
    std::unordered_map<char, int> badCharTable = build_bad_char_table(pattern);
    std::vector<int> goodSuffixTable = build_good_suffix_table(pattern);

    int s = 0;
    while (s <= n - m) {
        int j = m - 1;

        while (j >= 0 && pattern[j] == text[s + j]) {
            --j;
        }

        if (j < 0) {
            std::cout << "The sample was found at the position: " << s << std::endl;
            s += goodSuffixTable[m - 1];
        }
        else {
            int badCharShift = badCharTable.find(text[s + j]) != badCharTable.end()
                ? badCharTable[text[s + j]] - (m - 1 - j)
                : 1;
            s += std::max(goodSuffixTable[j], badCharShift);
        }
        }
    }

int main() {
    std::string text = "ababcababacababcababacababcababacababcababacababcababacababcababacababcababac";
    std::string pattern = "ababac";

    boyer_moore_search(text, pattern);

    return 0;
}

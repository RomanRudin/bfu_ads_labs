// #include "lab3.h"
#include <iostream>
#include <vector>
#include <string>
#include <map>

std::vector<std::map<char, int>> build_transition_table(const std::string& pattern) {
    int m = pattern.length();
    std::vector<std::map<char, int>> transitionTable(m + 1);

    for (int state = 0; state <= m; state++) {
        for (char c : {'a', 'b', 'c'}) {  
            int nextState = std::min(m, state + 1);
            while (nextState > 0 && pattern[nextState - 1] != c) {
                nextState = transitionTable[nextState - 1][c];
            }
            transitionTable[state][c] = nextState;
        }
    }

    return transitionTable;
}

void search_pattern(const std::string& text, const std::string& pattern) {
    std::vector<std::map<char, int>> transitionTable = build_transition_table(pattern);
    int n = text.length();
    int m = pattern.length();
    int state = 0;

    for (int i = 0; i < n; ++i) {
        char currentChar = text[i];
        if (transitionTable[state].find(currentChar) != transitionTable[state].end()) {
            state = transitionTable[state][currentChar];
        }
        else {
            state = 0;
        }

        if (state == m) {
            std::cout << "The sample was found at the position:" << i - m + 1 << std::endl;
        }
    }
}

int main() {
    std::string text = "ababcababacababcababacababcababacababcababacababcababacababcababacababcababac";
    std::string pattern = "ababac";

    search_pattern(text, pattern);

    return 0;
}


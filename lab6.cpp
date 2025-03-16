#include "lab6.h" 
#include <iostream>
#include <string>

const int PRIME = 101;  
const int ALPHABET_SIZE = 256;

long calculate_hash(const std::string& str, int length) {
    long hash = 0;
    for (int i = 0; i < length; ++i) {
        hash = (hash * ALPHABET_SIZE + str[i]) % PRIME;
    }
    return hash;
}
long power(int base, int exponent) {
    long result = 1;
    for (int i = 0; i < exponent; ++i) {
        result = (result * base) % PRIME;
    }
    return result;
}
long recalculate_hash(long oldHash, char oldChar, char newChar, int patternLength) {
    long newHash = (oldHash - oldChar * power(ALPHABET_SIZE, patternLength - 1)) % PRIME;
    newHash = (newHash * ALPHABET_SIZE + newChar) % PRIME;
    return (newHash < 0) ? newHash + PRIME : newHash;
}
void Rabin_karp_search(const std::string& text, const std::string& pattern) {
    int n = text.length();
    int m = pattern.length();
    long patternHash = calculate_hash(pattern, m);
    long textHash = calculate_hash(text, m);

    for (int i = 0; i <= n - m; ++i) {
        if (patternHash == textHash) {
            bool match = true;
            for (int j = 0; j < m; ++j) {
                if (text[i + j] != pattern[j]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                std::cout << "The sample was found at the position: " << i << std::endl;
            }
        }
        if (i < n - m) {
            textHash = recalculate_hash(textHash, text[i], text[i + m], m);
        }
    }
}

int main() {
    std::string text = "ababcababacababcababacababcababacababcababacababcababacababcababacababcababac";
    std::string pattern = "ababac";

    Rabin_karp_search(text, pattern);

    return 0;
}

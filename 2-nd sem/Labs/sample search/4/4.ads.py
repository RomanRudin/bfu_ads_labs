"""
Реализовать алгоритм Кнута-Морриса-Пратта для поиска по образцу.
Использовать префикс-функцию. Нужно понимать, что она значит (её определение).
Понимать, как она строится.
"""


def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
        else:
            pi[i] = 0
    return pi


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return 0
    pi = compute_prefix_function(pattern)
    j = 0

    occurrences = []
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i - m + 1)
            j = pi[j - 1]
    return occurrences


text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(kmp_search(text, pattern))

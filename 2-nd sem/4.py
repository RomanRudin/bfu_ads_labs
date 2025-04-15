def compute_lps_array(pattern):
    lps = [0] * len(pattern)
    length = 0
    for i in range(1, len(pattern)):
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
        else:
            lps[i] = 0
    return lps


def kmp_search(text, pattern):
    if not pattern:
        return []
    lps = compute_lps_array(pattern)
    i = 0
    j = 0
    occurrences = []
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                occurrences.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return occurrences


text = input("Введите текст: ")
pattern = input("Введите образец для поиска: ")
result = kmp_search(text, pattern)
if result:
    print(f"Образец найден на позициях: {result}")
else:
    print("Образец не найден в тексте.")

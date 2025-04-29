# Реализовать алгоритм Бойера-Мура для поиска по образцу
def boyer_moore_search(text, pattern):
    len_pat = len(pattern)
    len_text = len(text)

    # Если образец пустой или длиннее текста, возвращаем -1
    if len_pat == 0 or len_pat > len_text:
        return -1

    # Таблица плохих символов
    bad_char = {}
    for i in range(len_pat):
        bad_char[pattern[i]] = i

    # Таблица хороших суффиксов
    good_suffix = [0] * (len_pat + 1)
    border = [0] * (len_pat + 1)
    border[len_pat] = len_pat + 1
    i = len_pat
    j = len_pat + 1

    while i > 0:
        while j <= len_pat and pattern[i - 1] != pattern[j - 1]:
            if good_suffix[j] == 0:
                good_suffix[j] = j - i
            j = border[j]
        i -= 1
        j -= 1
        border[i] = j

    j = border[0]
    for i in range(len_pat + 1):
        if good_suffix[i] == 0:
            good_suffix[i] = j
        if i == j:
            j = border[j]

    i = 0
    while i <= len_text - len_pat:
        j = len_pat - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i
        else:
            bad_char_shift = j - bad_char.get(text[i + j], -1)
            good_suffix_shift = good_suffix[j + 1]
            i += max(bad_char_shift, good_suffix_shift)

    return -1


# Тест
if __name__ == "__main__":
    test_cases = [
        ("ABAAABCDABCABCDABCDABDE", "ABCDABD", 15),
        ("hello world", "world", 6),
        ("abcabcabc", "abc", 0),
        ("abcdefg", "xyz", -1),
        ("mississippi", "issi", 1),
        ("", "pattern", -1),
        ("text", "", -1)
    ]

    for text, pattern, expected in test_cases:
        result = boyer_moore_search(text, pattern)
        print(f"Текст: '{text}', Образец: '{pattern}'")
        print(f"Ожидаемый результат: {expected}, Полученный результат: {result}")
        print("Верно" if result == expected else "Ошибка")
        print()

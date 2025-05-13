# Реализовать алгоритм Рабина-Карпа для поиска по образцу.
# Здесь хэши, на автомат время работы должно быть линейное (пересчет хеша за O(1)).

def rabin_karp(text, pattern):
    d = 256  # Размер алфавита (ASCII)
    q = 101

    n = len(text)
    m = len(pattern)
    result = []

    if m == 0 or n < m:
        return result
    h = 1
    for _ in range(m - 1):
        h = (h * d) % q

    hash_pattern = 0
    hash_window = 0
    for i in range(m):
        hash_pattern = (d * hash_pattern + ord(pattern[i])) % q
        hash_window = (d * hash_window + ord(text[i])) % q

    for i in range(n - m + 1):
        if hash_pattern == hash_window:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                result.append(i)

        if i < n - m:
            hash_window = (d * (hash_window - ord(text[i]) * h) + ord(text[i + m])) % q
            if hash_window < 0:
                hash_window += q

    return result


if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABD"
    print(f"Текст: {text}")
    print(f"Образец: {pattern}")

    result = rabin_karp(text, pattern)
    if result:
        print(f"Образец найден на позициях: {result}")
    else:
        print("Образец не найден")

"""
Реализовать алгоритм поиска по образцу с помощью конечного автомата.
Автомат по префикс функции.
"""

def build_finite_automaton(pattern):
    m = len(pattern)
    alphabet = set(pattern)
    prefix = [0] * m
    transition = [{} for _ in range(m + 1)]
    for i in range(1, m):
        j = prefix[i - 1]
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j

    for state in range(m + 1):
        for char in alphabet:
            if state < m and char == pattern[state]:
                next_state = state + 1
            else:
                next_state = 0
                if state > 0:
                    next_state = transition[prefix[state - 1]].get(char, 0)
            transition[state][char] = next_state

    return transition


def finite_automaton_search(text, pattern):
    m = len(pattern)
    if m == 0:
        return []

    transition = build_finite_automaton(pattern)
    state = 0
    occurrences = []

    for i, char in enumerate(text):
        state = transition[state].get(char, 0)
        if state == m:
            occurrences.append(i - m + 1)

    return occurrences


if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"

    print(f"Текст: {text}")
    print(f"Образец: {pattern}")

    result = finite_automaton_search(text, pattern)

    if result:
        print(f"Образец найден на позициях: {result}")
    else:
        print("Образец не найден в тексте")

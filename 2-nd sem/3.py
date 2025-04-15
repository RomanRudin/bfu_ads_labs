def build_finite_automaton(pattern):
    m = len(pattern)
    transition = [{} for _ in range(m + 1)]
    for state in range(m + 1):
        for char in set(pattern):
            next_state = min(m, state + 1)
            while next_state > 0 and pattern[:next_state] != (pattern[:state] + char)[-next_state:]:
                next_state -= 1
            transition[state][char] = next_state
    return transition


def finite_automaton_search(text, pattern):
    if not pattern:
        return 0
    transition = build_finite_automaton(pattern)
    m = len(pattern)
    n = len(text)
    state = 0
    for i in range(n):
        char = text[i]
        state = transition[state].get(char, 0)
        if state == m:
            return i - m + 1
    return -1


if __name__ == "__main__":
    print("Алгоритм поиска по образцу с помощью конечного автомата")
    text = input("Введите текст для поиска: ")
    pattern = input("Введите образец для поиска: ")
    position = finite_automaton_search(text, pattern)
    if position != -1:
        print(f"Образец найден в позиции {position} (индексация с 0)")
    else:
        print("Образец не найден в тексте")

def build_transition_table(pattern: str) -> list[dict]:
    m = len(pattern)
    unique_chars = set(pattern)
    transition_table = [{} for _ in range(m + 1)]
    
    for state in range(m + 1):
        for c in unique_chars:
            next_state = min(m, state + 1)
            while next_state > 0 and pattern[next_state - 1] != c:
                next_state = transition_table[next_state - 1].get(c, 0)
            transition_table[state][c] = next_state
    
    return transition_table

def finite_automata(text: str, pattern: str) -> None:
    if len(pattern) == 0:
        return list(range(len(text) + 1))
    if len(text) < len(pattern):
        return []
    
    transition_table = build_transition_table(pattern)
    n = len(text)
    m = len(pattern)
    state = 0
    
    occurrences = []
    
    for i, c in enumerate(text):
        state = transition_table[state].get(c, 0)
        if state == m:
            occurrences.append(i - m + 1)
    
    return occurrences



if __name__ == "__main__":
    print(f"Result of bm_algorythm: {finite_automata('abca', 'abca')}")
    print(f"Result of bm_algorythm: {finite_automata('abcababdabaaba', 'abaaba')}")
    print(f"Result of bm_algorythm: {finite_automata('abcababdabaabadd', 'abaaba')}")
    print(f"Result of bm_algorythm: {finite_automata('abcababdabaabadd', 'aba')}")

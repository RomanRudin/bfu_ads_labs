def build_transition_table(pattern: str) -> list[dict]:
    m = len(pattern)
    transition_table = [{} for _ in range(m + 1)]
    
    for state in range(m + 1):
        for c in ['a', 'b', 'c']:
            next_state = min(m, state + 1)
            while next_state > 0 and (next_state - 1 >= len(pattern) or pattern[next_state - 1] != c):
                next_state = transition_table[next_state - 1].get(c, 0)
            transition_table[state][c] = next_state
    
    return transition_table

def finite_automata(text: str, pattern: str) -> None:
    transition_table = build_transition_table(pattern)
    n = len(text)
    m = len(pattern)
    state = 0
    
    for i in range(n):
        current_char = text[i]
        state = transition_table[state].get(current_char, 0)
        
        if state == m:
            return i - m + 1



if __name__ == "__main__":
    print(f"Result of bm_algorythm: {finite_automata('abca', 'abca')}")
    print(f"Result of bm_algorythm: {finite_automata('abcababdabaaba', 'abaaba')}")
    print(f"Result of bm_algorythm: {finite_automata('abcababdabaabadd', 'abaaba')}")
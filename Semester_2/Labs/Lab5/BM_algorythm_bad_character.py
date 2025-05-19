def preprocess_bad_char(pattern: str) -> dict[str, int]:
    bad_char = {}
    for i, char in enumerate(pattern):
        bad_char[char] = i
    return bad_char

def bm_search(text: str, pattern: str) -> list[int]:
    if not pattern or not text:
        return []
    
    bad_char = preprocess_bad_char(pattern)
    m = len(pattern)
    n = len(text)
    result = []
    
    shift = 0
    while shift <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
            
        if j < 0:
            result.append(shift)
            shift += (m - bad_char.get(text[shift + m], -1)) if shift + m < n else 1
        else:
            char = text[shift + j]
            shift += max(1, j - bad_char.get(char, -1))
    
    return result

if __name__ == "__main__":
    print(f"Result of bm_algorythm: {bm_search('abca', 'abca')}")
    print(f"Result of bm_algorythm: {bm_search('abcababdabaaba', 'abaaba')}")
    print(f"Result of bm_algorythm: {bm_search('abcababdabaabadd', 'abaaba')}")

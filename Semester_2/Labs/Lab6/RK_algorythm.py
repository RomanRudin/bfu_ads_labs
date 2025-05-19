def rk_algorithm(text: str, pattern: str, base: int = 256, prime: int = 101) -> list[int]:
    n = len(text)
    m = len(pattern)
    result = []
    
    if m == 0 or n < m:
        return result
    
    h = 1
    for _ in range(m-1):
        h = (h * base) % prime
    
    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        window_hash = (base * window_hash + ord(text[i])) % prime
    
    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if pattern == text[i:i+m]:
                result.append(i)
        
        if i < n - m:
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i+m])) % prime
            if window_hash < 0:
                window_hash += prime
    
    return result

if __name__ == "__main__":
    print(f"Result of rk_algorythm: {rk_algorythm('abca', 'abca')}")
    print(f"Result of rk_algorythm: {rk_algorythm('abcababdabaaba', 'abaaba')}")
    print(f"Result of rk_algorythm: {rk_algorythm('abcababdabaab', 'abaaba')}")
    print(f"Result of rk_algorythm: {rk_algorythm('abcababdabaab', 'ab')}")

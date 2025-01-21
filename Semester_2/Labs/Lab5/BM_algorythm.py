def get_substring(text: str, pattern: str) -> list[int]: 
    result = []
    alphabet_size = 256
    mod = 9973
    pattern_hash = pattern.charCodeAt(0) % mod
    text_hash = text.charCodeAt(0) % mod
    first_index_hash = 1

    for i in range(1, len(pattern)):
        pattern_hash *= alphabet_size
        pattern_hash += pattern.charCodeAt(i)
        pattern_hash %= mod

        text_hash *= alphabet_size
        text_hash += text.charCodeAt(i)
        text_hash %= mod

        first_index_hash *= alphabet_size
        first_index_hash %= mod

    for i in range(0, len(text) - len(pattern) + 1):
        if ((pattern_hash == text_hash) and (compareText(text, i, pattern))):
            result.push(i)

        if (i == len(text) - len(pattern)): break

        text_hash -= (text.charCodeAt(i) * first_index_hash) % mod
        text_hash += mod
        text_hash *= alphabet_size
        text_hash += text.charCodeAt(i + pattern.length)
        text_hash %= mod
    return result

def compareText(text: str, index: int, pattern: str) -> bool:
    for i in range(len(pattern)):
        if (pattern[i] != text[index + i]):
            return False
    return True
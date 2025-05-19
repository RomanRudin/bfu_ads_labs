def find_borders(pattern: str) -> list[int]: 
    if not pattern:
        return []
    
    borders = [0] * len(pattern)
    current_index = 0
    for i in range(1, len(pattern)):
        while current_index > 0 and pattern[current_index] != pattern[i]:
            current_index = borders[current_index - 1]
        if (pattern[current_index] == pattern[i]):
            current_index += 1
        borders[i] = current_index
    return borders


def kmp_algorythm(text: str, pattern: str) -> list[int]:
    if not pattern:
        return []
    if len(pattern) > len(text):
        return []
    
    borders = find_borders(pattern)
    print(borders)
    result = []
    compare_index = 0

    for i, char in enumerate(text):
        while compare_index > 0 and char != pattern[compare_index]:
            compare_index = borders[compare_index - 1]
            
        if char == pattern[compare_index]:
            compare_index += 1
            
        if compare_index == len(pattern):
            result.append(i - compare_index + 1)
            compare_index = borders[compare_index - 1]

    return result

if __name__ == "__main__":
    print(f"Result of kmp_algorythm: {kmp_algorithm('abca', 'abca')}")
    print(f"Result of kmp_algorythm: {kmp_algorithm('abcababdabaaba', 'abaaba')}")
    print(f"Result of kmp_algorythm: {kmp_algorithm('', 'abc')}")

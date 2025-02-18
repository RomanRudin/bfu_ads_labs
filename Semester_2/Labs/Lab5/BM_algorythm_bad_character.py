def get_bad_characters_dict(pattern: str) -> dict[str, int]:
    bad_characters_dict = {}

    for i in range(len(pattern)):
        bad_characters_dict[pattern[i]] = i

    return bad_characters_dict



def bm_algorythm_bad_character(text: str, pattern: str) -> list[int]:
    symbol_indexes = get_bad_characters_dict(pattern)
    result = []
    shift = 0

    while (shift <= (len(text) - len(pattern))):
        current_index = len(pattern) - 1
        while (current_index >= 0 and pattern[current_index] == text[shift + current_index]):
            current_index -= 1

        if (current_index == -1):
            result.append(shift)
            if (shift + len(pattern)) < len(text):
                shift += len(pattern) - symbol_indexes[text[shift + len(pattern)]]
            else:
                shift += 1

        else:
            if text[shift + current_index] in symbol_indexes.keys():
                indent = symbol_indexes[text[shift + current_index]]
            else:
                indent = -1
            shift += max(1, current_index - indent)

    return result

if __name__ == "__main__":
    print(f"Result of bm_algorythm: {bm_algorythm_bad_character('abca', 'abca')}")
    print(f"Result of bm_algorythm: {bm_algorythm_bad_character('abcababdabaaba', 'abaaba')}")

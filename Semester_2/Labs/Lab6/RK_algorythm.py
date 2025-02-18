# def compareText(text: str, index: int, pattern: str) -> bool:
#     for i, sym in enumerate(pattern):
#         if (sym != text[index + i]):
#             return False
#     return True


def rk_algorythm(text: str, pattern: str) -> list[int]:
    result = []
    patternHash = hash(pattern)

    for i in range(len(text) - len(pattern) + 1):
        textHash = hash(text[i:(len(pattern) + i)])
        # print(f"i = {i} \t {pattern} : {patternHash}, \t {text[i:(len(pattern) + i)]} : {textHash}")
        if ((patternHash == textHash) and all([pattern[j] == text[i + j] for j in range(len(pattern))])):
            result.append(i)
    return result

# if __name__ == "__main__":
#     print(f"Result of rk_algorythm: {rk_algorythm('abca', 'abca')}")
#     print(f"Result of rk_algorythm: {rk_algorythm('abcababdabaaba', 'abaaba')}")

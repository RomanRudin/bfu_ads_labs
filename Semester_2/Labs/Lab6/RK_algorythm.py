def compareText(text: str, index: int, pattern: str) -> bool:
    for i in range(len(pattern)):
        if (pattern[i] != text[index + i]):
            return False
    return True



def rk_algorythm(text: str, pattern: str) -> list[int]:
    result = []
    alphabetSize = 256
    mod = 9973

    patternHash = ord(pattern[0]) % mod
    textHash = ord(text[0]) % mod

    firstIndexHash = 1

    for i in range(1, len(pattern)):
        patternHash *= alphabetSize
        patternHash += ord(pattern[i])
        patternHash %= mod

        textHash *= alphabetSize
        textHash += ord(text[i])
        textHash %= mod

        firstIndexHash *= alphabetSize
        firstIndexHash %= mod

    for i in range(len(text) - len(pattern)):
        if ((patternHash == textHash) and compareText(text, i, pattern)):
            result.append(i)

        if (i == len(text) - len(pattern)): break

        textHash -= (ord(text[i]) * firstIndexHash) % mod
        textHash += mod
        textHash *= alphabetSize
        textHash += ord(text[i + len(pattern)])
        textHash %= mod

    return result
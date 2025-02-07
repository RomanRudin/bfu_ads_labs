def bm_algorythm_good_suffix(text: str, pattern: str) -> list[int]:
    pass

def get_good_suffix_array(pattern: str)-> list[int]:
    shifts = [0] * (len(pattern )+ 1)
    borderPositions = [0] * (len(pattern) + 1)

    find_shifts_and_borders(shifts, borderPositions, pattern)

    set_shifts_for_prefix(shifts, borderPositions, pattern)

    return shifts

def find_shifts_and_borders(shifts: list[int], borderPositions: list[int], pattern: str) -> None: 
    i, j = len(pattern), len(pattern) + 1
    borderPositions[i] = j

    while (i > 0):
        while (j <= pattern.length and pattern[i - 1] != pattern[j - 1]):
            if (shifts[j] == 0):
                shifts[j] = j - i

            j = borderPositions[j]

        i -= 1
        j -= 1

        borderPositions[i] = j

def set_shifts_for_prefix(shifts: list[int], borderPositions: list[int], pattern: str) -> None:
    prefixBorder = borderPositions[0]

    for i in range(len(pattern)):
        if (shifts[i] == 0):
            shifts[i] = prefixBorder

        if (i == prefixBorder):
            prefixBorder = borderPositions[prefixBorder]
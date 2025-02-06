def bm_algorythm_good_suffix(text: str, pattern: str) -> list[int]:
export function goodSuffixHeuristic(pattern: string): number[] {
    const shifts = new Array(pattern.length + 1).fill(0);
    const borderPositions = new Array(pattern.length + 1);

    findShiftsAndBorders(shifts, borderPositions, pattern);

    setShiftsForPrefix(shifts, borderPositions, pattern);

    return shifts;
}

function findShiftsAndBorders(shifts: number[], borderPositions: number[], pattern: string): void {
    let i = pattern.length;
    let j = pattern.length + 1;

    borderPositions[i] = j;

    while (i > 0) {
        while (j <= pattern.length && pattern[i - 1]!== pattern[j - 1]) {
            if (shifts[j] === 0) {
                shifts[j] = j - i;
            }

            j = borderPositions[j];
        }

        i--;
        j--;

        borderPositions[i] = j;
    }
}

function setShiftsForPrefix(shifts: number[], borderPositions: number[], pattern: string): void {
    let prefixBorder = borderPositions[0];

    for (let i = 0; i <= pattern.length; i++) {
        if (shifts[i] === 0) {
            shifts[i] = prefixBorder;
        }

        if (i === prefixBorder) {
            prefixBorder = borderPositions[prefixBorder];
        }
    }
}
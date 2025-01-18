def max_subarray(array: list) -> tuple[list, float]:
    max_sum = float('-inf')
    sum = 0
    starting_index, ending_index = 0, 0

    for index, elem in enumerate(array):
        sum += elem
        if sum > max_sum:
            max_sum = sum
            ending_index = index
        if sum < 0:
            sum = 0
            starting_index = index + 1

    return (array[starting_index:ending_index + 1], max_sum)
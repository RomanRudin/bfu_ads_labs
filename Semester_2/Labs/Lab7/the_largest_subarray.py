def the_largest_subarray(array: list) -> tuple[list, float]:
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


if __name__ == "__main__":
    print(f"Result: {the_largest_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])}") #? Expected [4, -1, 2, 1], 6
    print(f"Result: {the_largest_subarray([2, -1, 2, -1, 2])}") #? Expected [2, -1, 2, -1, 2], 4
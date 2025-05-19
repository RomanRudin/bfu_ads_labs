def the_largest_subarray(array: list) -> tuple[list, float]:
    max_sum = current_sum = array[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(array)):
        if array[i] > current_sum + array[i]:
            current_sum = array[i]
            temp_start = i
        else:
            current_sum += array[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    return (array[start:end + 1], max_sum)


if __name__ == "__main__":
    print(f"Result: {the_largest_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])}") #? Expected [4, -1, 2, 1], 6
    print(f"Result: {the_largest_subarray([2, -1, 2, -1, 2])}") #? Expected [2, -1, 2, -1, 2], 4
    print(f"Result: {the_largest_subarray([-2, -1, -2, -1, -2])}") #? Expected [-1], -1

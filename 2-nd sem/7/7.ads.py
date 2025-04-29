# Задача о самом большом подмассиве: поиск непрерывного подмассива в одномерном массиве чисел с наибольшей суммой.

def max_subarray_with_indices(nums):
    if not nums:
        return 0, -1, -1

    if all(x < 0 for x in nums):
        max_val = max(nums)
        index = nums.index(max_val)
        return max_val, index, index

    max_current = max_global = nums[0]
    start = end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > max_current + nums[i]:
            max_current = nums[i]
            temp_start = i
        else:
            max_current += nums[i]
        if max_current > max_global:
            max_global = max_current
            start = temp_start
            end = i

    return max_global, start, end


if __name__ == "__main__":
    print("\nПервый пример:")
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, start_idx, end_idx = max_subarray_with_indices(arr)
    print(f"Максимальная сумма подмассива: {max_sum}")
    print(f"Начальный индекс: {start_idx}, Конечный индекс: {end_idx}")
    print(f"Подмассив: {arr[start_idx:end_idx + 1]}")
    arr_neg = [-3, -1, -8, -2, -5]
    max_sum_neg, start_neg, end_neg = max_subarray_with_indices(arr_neg)
    print("\nС отрицательными числами:")
    print(f"Максимальная сумма: {max_sum_neg}")
    print(f"Начальный индекс: {start_neg}, Конечный индекс: {end_neg}")
    print(f"Подмассив: {arr_neg[start_neg]}")

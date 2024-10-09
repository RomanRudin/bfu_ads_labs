def separate_negative(arr: list) -> list[list]:
    return [elem for elem in arr if elem < 0], [elem for elem in arr if elem >= 0]


def radix_sort(arr: list) -> list:
    negative_arr, positive_arr = separate_negative(arr)
    
    #for negative numbers:
    if len(negative_arr) > 0:
        max_digits = max(len(str(elem)) - 1 for elem in negative_arr)
        radix = [[] for _ in range(10)]
        for exponent in range(max_digits):
            for elem in negative_arr:
                radix[(elem // 10 ** exponent) % 10].append(elem)
            negative_arr = [elem for bucket in radix for elem in bucket]
            radix = [[] for _ in range(10)]

    #for positive numbers:
    if len(positive_arr) > 0:
        max_digits = max(len(str(elem)) for elem in positive_arr)
        radix = [[] for _ in range(10)]
        for exponent in range(max_digits):
            for elem in positive_arr:
                radix[(elem // 10 ** exponent) % 10].append(elem)
            positive_arr = [elem for bucket in radix for elem in bucket]
            radix = [[] for _ in range(10)]

    return negative_arr + positive_arr
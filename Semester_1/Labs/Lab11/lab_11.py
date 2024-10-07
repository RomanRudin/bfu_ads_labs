def quick_sort(arr: list) -> list:
    if (len(arr) < 2): return arr
    pivotal = arr.pop(0)
    left, right = [], []
    for elem in arr:
        if (pivotal > elem): 
            left.append(elem)
        else:
            right.append(elem)
    answer = quick_sort(left)
    answer.append(pivotal)
    answer.extend(quick_sort(right))
    return answer
# Check https://thecode.media/comb-sort/ firstly
def comb_sort(arr):
    gap = len(arr)
    shrink = 1.247
    sorted = False
    while gap >= 1 or not sorted:
        gap = int(gap / shrink)
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
        if gap >= 1:
            sorted = True
    return arr


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(comb_sort(arr))
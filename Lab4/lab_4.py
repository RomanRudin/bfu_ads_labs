# Check https://thecode.media/comb-sort/ firstly

def comb_sort(arr):
    shrink = 1.247
    gapFactor = len(arr) / shrink
    while gapFactor > 1:
        gap = int(gapFactor)
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
        gapFactor /= shrink
    return arr

# arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(comb_sort(arr))
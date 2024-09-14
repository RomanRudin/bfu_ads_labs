
# from heapq import heapify
# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап
        heapify(arr, n, largest)

def heap_sort(arr:list) -> list:
    for i in range(len(arr), -1, -1):
        heapify(arr, len(arr), i)
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап 
        heapify(arr, i, 0)
    return arr
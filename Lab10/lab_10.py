# Extra function can be replaced by extend() method of list, but I wanted to understand algorythm better
def merge(left: list, right: list) -> list:
    arr = []
    while (len(left) and len(right)):
        if (left[0] < right[0]):
            arr.append(left.pop(0))  
        else:
            arr.append(right.pop(0)) 
    if len(left):
        arr.extend(left)
    if len(right):
        arr.extend(right)
    return arr

def merge_sort(arr: list) -> list:
  if(len(arr) < 2):  return arr 
  half = int(len(arr) / 2)
  return merge(merge_sort(arr[:half]),merge_sort(arr[half:]))
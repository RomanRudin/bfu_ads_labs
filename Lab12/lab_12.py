def external_multiphase_sort(arr: list) -> list:
    # fibonacci series is used to find the distance of each phase
    fibonacci_series = [0, 1]  
    while fibonacci_series[-1] < len(arr):  
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])  
  
    def sort_phase(arr, distance):  
        for i in range(distance, len(arr)):  
            j = i  
            while j > 0 and arr[j] < arr[j - distance]:  
                arr[j], arr[j - distance] = arr[j - distance], arr[j]  
                j -= distance  
  
    # Sorting each phase independently
    for distance in fibonacci_series[::-1]:  
        sort_phase(arr, distance)  
    return arr
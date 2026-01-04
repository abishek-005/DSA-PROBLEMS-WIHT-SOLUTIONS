import time
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
    return result
# Example usage
unsorted_list = [64, 34, 25, 12, 22, 11, 90,6,3526,46,34,867,1,5,7,234,7,4,6,56,4,6]
sorted_list = measure_time(selection_sort,unsorted_list)
print("Sorted array:", sorted_list)

import time
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
    return result
# Example usage
unsorted_list = [64, 34, 25, 12, 22, 11, 90,6,3526,46,34,867,1,5,7,234,7,4,6,56,4,6]
sorted_list = measure_time(quicksort,unsorted_list)
print("Sorted array:", sorted_list)

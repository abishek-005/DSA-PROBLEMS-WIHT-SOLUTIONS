import time
import random
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
# Test with different array sizes
sizes = [100, 1000, 10000]
for size in sizes:
    arr = [random.randint(1, 1000) for _ in range(size)]
    # Measure Selection Sort time
    start = time.time()
    selection_sort(arr.copy())
    selection_time = time.time() - start
    # Measure Quicksort time
    start = time.time()
    quicksort(arr.copy())
    quicksort_time = time.time() - start
    print(f"Array size: {size}")
print(f"Selection Sort time: {selection_time:.6f} seconds")
print(f"Quicksort time: {quicksort_time:.6f} seconds")
print()

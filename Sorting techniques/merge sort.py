import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    # compare pannitu chinna value add pannrom
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # left side la balance irundha
    result.extend(left[i:])
    # right side la balance irundha
    result.extend(right[j:])

    return result


def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")
    return result


# Example usage
unsorted_list = [64, 34, 25, 12, 22, 11, 90]

sorted_list = measure_time(merge_sort, unsorted_list)

print("Sorted list:", sorted_list)

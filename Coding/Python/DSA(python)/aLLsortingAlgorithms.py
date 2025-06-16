# # Bubble Sort: Repeatedly swaps adjacent elements if they are in wrong order
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# # Selection Sort: Finds minimum element and places it at the beginning
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# # Insertion Sort: Builds sorted array one item at a time
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# # Merge Sort: Divides array into halves, sorts, and merges
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# # Quick Sort: Picks a pivot and partitions array around it
# def quick_sort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quick_sort(arr, low, pi - 1)
#         quick_sort(arr, pi + 1, high)
#     return arr

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

# # Heap Sort: Builds max heap and extracts elements to sort
# def heap_sort(arr):
#     def heapify(arr, n, i):
#         largest = i
#         left = 2 * i + 1
#         right = 2 * i + 2
#         if left < n and arr[left] > arr[largest]:
#             largest = left
#         if right < n and arr[right] > arr[largest]:
#             largest = right
#         if largest != i:
#             arr[i], arr[largest] = arr[largest], arr[i]
#             heapify(arr, n, largest)
    
#     n = len(arr)
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n - 1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, i, 0)
#     return arr

# # Example usage
# if __name__ == "__main__":
#     arr = [64, 34, 25, 12, 22, 11, 90]
#     print("Original array:", arr)
#     print("Bubble Sort:", bubble_sort(arr.copy()))
#     print("Selection Sort:", selection_sort(arr.copy()))
#     print("Insertion Sort:", insertion_sort(arr.copy()))
#     print("Merge Sort:", merge_sort(arr.copy()))
#     print("Quick Sort:", quick_sort(arr.copy(), 0, len(arr) - 1))
#     print("Heap Sort:", heap_sort(arr.copy()))














# import time
# import random

# # Bubble Sort
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# # Selection Sort
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# # Insertion Sort
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# # Merge Sort
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# # Quick Sort
# def quick_sort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quick_sort(arr, low, pi - 1)
#         quick_sort(arr, pi + 1, high)
#     return arr

# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

# # Heap Sort
# def heap_sort(arr):
#     def heapify(arr, n, i):
#         largest = i
#         left = 2 * i + 1
#         right = 2 * i + 2
#         if left < n and arr[left] > arr[largest]:
#             largest = left
#         if right < n and arr[right] > arr[largest]:
#             largest = right
#         if largest != i:
#             arr[i], arr[largest] = arr[largest], arr[i]
#             heapify(arr, n, largest)
    
#     n = len(arr)
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n - 1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, i, 0)
#     return arr

# # Function to measure sorting time
# def measure_time(sort_func, arr, *args):
#     start_time = time.time()
#     if sort_func == quick_sort:
#         result = sort_func(arr.copy(), 0, len(arr) - 1)
#     else:
#         result = sort_func(arr.copy(), *args)
#     end_time = time.time()
#     return end_time - start_time, result

# # Example usage
# if __name__ == "__main__":
#     # Generate a random array
#     random.seed(42)  # For reproducibility
#     arr = [random.randint(1, 1000) for _ in range(1000)]  # Array of 1000 elements
    
#     print("Sorting times for array of size", len(arr))
#     print("-" * 40)
    
#     # Measure time for each sorting algorithm
#     algorithms = [
#         ("Bubble Sort", bubble_sort),
#         ("Selection Sort", selection_sort),
#         ("Insertion Sort", insertion_sort),
#         ("Merge Sort", merge_sort),
#         ("Quick Sort", quick_sort),
#         ("Heap Sort", heap_sort)
#     ]
    
#     for name, func in algorithms:
#         time_taken, sorted_arr = measure_time(func, arr)
#         print(f"{name}: {time_taken:.6f} seconds")
#         # Verify sorting is correct
#         assert sorted_arr == sorted(arr), f"{name} failed to sort correctly"














import time
import random

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Heap Sort
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

# Function to measure sorting time
def measure_time(sort_func, arr, *args):
    start_time = time.time()
    if sort_func == quick_sort:
        result = sort_func(arr.copy(), 0, len(arr) - 1)
    else:
        result = sort_func(arr.copy(), *args)
    end_time = time.time()
    return end_time - start_time, result

# Collect timing data
if __name__ == "__main__":
    random.seed(42)  # For reproducibility
    arr = [random.randint(1, 1000) for _ in range(1000)]  # Array of 1000 elements
    times = {}
    
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort)
    ]
    
    print("Sorting times for array of size", len(arr))
    print("-" * 40)
    
    for name, func in algorithms:
        time_taken, sorted_arr = measure_time(func, arr)
        times[name] = time_taken
        print(f"{name}: {time_taken:.6f} seconds")
        assert sorted_arr == sorted(arr), f"{name} failed to sort correctly"
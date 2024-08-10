import heapq

# Creating a min heap
min_heap = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
heapq.heapify(min_heap)
print("Min Heap:", min_heap)

# Creating a max heap
max_heap = [-3, -5, -9, -6, -8, -20, -10, -12, -18, -9]
heapq.heapify(max_heap)
max_heap = [-i for i in max_heap]
heapq.heapify(max_heap)
print("Max Heap:", max_heap)

# Inserting elements into the min heap
heapq.heappush(min_heap, 1)
print("Min Heap after insertion:", min_heap)

# Removing elements from the min heap
min_element = heapq.heappop(min_heap)
print("Min Heap after removal:", min_heap)
print("Removed element:", min_element)

# Inserting elements into the max heap
heapq.heappush(max_heap, -1)
print("Max Heap after insertion:", max_heap)

# Removing elements from the max heap
max_element = -heapq.heappop(max_heap)
print("Max Heap after removal:", max_heap)
print("Removed element:", max_element)

# Creating a min heap without importing heapq

def heapify_min(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down_min(arr, i, n)

def sift_down_min(arr, i, n):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        sift_down_min(arr, smallest, n)

min_heap = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
heapify_min(min_heap)
print("Min Heap:", min_heap)

# Creating a max heap without importing heapq

def heapify_max(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down_max(arr, i, n)

def sift_down_max(arr, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        sift_down_max(arr, largest, n)

max_heap = [-3, -5, -9, -6, -8, -20, -10, -12, -18, -9]
heapify_max(max_heap)
max_heap = [-i for i in max_heap]
heapify_max(max_heap)
print("Max Heap:", max_heap)
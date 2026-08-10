import time

# Max Heapify
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


# Max Heap Sort
def heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Remove elements from Max Heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


# ---------------- USER INPUT ----------------

n = int(input("Enter number of elements: "))

arr = []

print("Enter", n, "elements:")

for i in range(n):
    arr.append(int(input("Element " + str(i + 1) + ": ")))


print("\nOriginal Array:", arr)

# Start execution time
start_time = time.perf_counter()

# Sorting
heap_sort(arr)

# End execution time
end_time = time.perf_counter()

execution_time = end_time - start_time


# ---------------- OUTPUT ----------------

print("\nSorted Array:", arr)

print("\n----- COMPLEXITY ANALYSIS -----")
print("Best Case Time Complexity    : O(n log n)")
print("Average Case Time Complexity : O(n log n)")
print("Worst Case Time Complexity   : O(n log n)")
print("Space Complexity             : O(log n)")

print("\nActual Execution Time:", execution_time, "seconds")
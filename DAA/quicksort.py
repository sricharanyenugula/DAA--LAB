import time

def partition(arr, low, high):
    pivot = arr[high]      # Last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Main Program
n = int(input("Enter number of elements: "))

print("Enter elements:")
arr = list(map(int, input().split()))

start = time.perf_counter()

quick_sort(arr, 0, n - 1)

stop = time.perf_counter()

print("\nSorted Array:")
print(*arr)

execution_time = (stop - start) * 1_000_000  # Convert to microseconds

print("\nTime Complexity:")
print("Best Case : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case : O(n²)")
print(f"Execution Time: {execution_time:.2f} microseconds")